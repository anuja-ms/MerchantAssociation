from datetime import datetime
from itertools import count
from django.shortcuts import render
from adminapp.models import tbl_district
from guestapp.models import Login
from adminapp.models import tbl_location,tbl_unit,tbl_member,tbl_welfare,tbl_notification,tbl_welfarepublish
from memberapp.models import tbl_loan,tbl_loantransaction, tbl_deposite, tbl_welfaretransaction
from django.http import HttpResponse,JsonResponse
from email.message import EmailMessage
import smtplib
from django.db.models import Count
import xlwt
from django.views.generic import View


# Create your views here.
import matplotlib.pyplot as plt
from io import BytesIO
from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from datetime import datetime
import calendar
 # Adjust the imports based on your models

def index(request):
    # Calculate the total of the 'deposite' field
    total_deposit = tbl_deposite.objects.aggregate(total=Sum('deposite'))['total']

    # If there are no deposits, set the total to 0
    if total_deposit is None:
        total_deposit = 0
    
    # Calculate the total number of members
    total_members = tbl_member.objects.count()

    # Get filter parameters from request (for loan transaction filtering)
    member_id = request.GET.get('member_id')
    installment_month = request.GET.get('installment_month')
    selected_month = request.GET.get('month')  # Get selected month

    # Start with all loan transactions
    loan = tbl_loantransaction.objects.all()

    # Apply filters if parameters exist
    if member_id:
        loan = loan.filter(loan_id__member_id=member_id)
    if installment_month:
        loan = loan.filter(loan_id__installmentmonths=installment_month)
    if selected_month:
        loan = loan.filter(paiddate__month=selected_month)  # Filter by month from paid date

    # Generate the deposit bar chart
    current_year = datetime.now().year
    months_list = list(range(1, 13))

    # Aggregate the deposits by month
    total_deposits = tbl_deposite.objects.annotate(month=TruncMonth('depositedate')) \
                                        .values('month') \
                                        .annotate(total_deposit=Sum('deposite')) \
                                        .order_by('month')

    # Prepare the data for plotting
    month_labels = [calendar.month_name[m] for m in months_list]
    totals = [0] * 12  # Initialize a list with 0 values for each month

    # Populate the totals list with actual deposit values for each month
    for entry in total_deposits:
        month_index = entry['month'].month - 1  # Get the index of the month (0-based)
        totals[month_index] = entry['total_deposit']

    # Create the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(month_labels, totals, color='blue')

    # Add labels and title
    plt.xlabel('Month')
    plt.ylabel('Total Deposit')
    plt.title(f'Total Deposits per Month for {current_year}')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the figure to a BytesIO object (in-memory image)
    img_io = BytesIO()
    plt.savefig(img_io, format='png')
    img_io.seek(0)  # Seek to the beginning of the BytesIO object

    # Prepare the chart image for rendering in the template
    chart_image = img_io.getvalue()

    # Pass the necessary data to the template
    return render(request, "admin/index.html", {
        'total_deposit': total_deposit,
        'total_members': total_members,
        'loan': loan,
        'selected_month': selected_month,
        'chart_image': chart_image  # Pass the chart image to the template
    })


def district(request):
    return render(request,"admin/district.html")

def district_process(request):
    if request.method == 'POST':
        districtname = request.POST.get("districtname")
        dob = tbl_district()
        dob.districtname = districtname
        if tbl_district.objects.filter(districtname=districtname).exists():
            return HttpResponse("<script>alert('Already Exist');window.location='/adminapp/viewdistrict';</script>")
        else:
            dob.save()
            return HttpResponse("<script>alert('Succesfully Inserted');window.location='/adminapp/viewdistrict';</script>")

def location(request):
    districts=tbl_district.objects.all()
    return render(request,"admin/location.html",{'districts':districts})

def location_process(request):
    if request.method == 'POST':
        district_id = request.POST.get("district_id")
        locationname = request.POST.get("locationname")
        lob = tbl_location()
        lob.locationname = locationname
        lob.district_id = tbl_district.objects.get(district_id=district_id)
        if tbl_location.objects.filter(locationname=locationname,district_id=district_id).exists():
            return HttpResponse("<script>alert('Already Exist');window.location='/adminapp/viewlocation';</script>")
        else:
            lob.save()
            return HttpResponse("<script>alert('Succesfully Inserted');window.location='/adminapp/viewlocation';</script>")

def unit(request):
    districts=tbl_district.objects.all()
    return render(request,"admin/unit.html",{'districts':districts})

def unit_process(request):
    if request.method == 'POST':
        district_id = request.POST.get("district_id")
        unitname = request.POST.get("unitname")
        uob = tbl_unit()
        uob.unitname = unitname
        uob.district_id = tbl_district.objects.get(district_id=district_id)
        if tbl_unit.objects.filter(unitname=unitname,district_id=district_id).exists():
            return HttpResponse("<script>alert('Already Exist');window.location='/adminapp/viewunit';</script>")
        else:
            uob.save()
            return HttpResponse("<script>alert('Succesfully Inserted');window.location='/adminapp/viewunit';</script>")

def viewdistrict(request):
    district=tbl_district.objects.all()
    return render(request,"admin/viewdistrict.html",{'district':district})

def viewlocation(request):
    districts=tbl_district.objects.all()
    return render(request,"admin/viewlocation.html",{'districts':districts})

def filllocation(request):
    did = int(request.POST.get("did"))
    location = tbl_location.objects.filter(district_id=did).values()
    return JsonResponse(list(location),safe=False)

def viewunit(request):
    districts=tbl_district.objects.all()
    return render(request,"admin/viewunit.html",{'districts':districts})

def fillunit(request):
    did = int(request.POST.get("did"))
    unit = tbl_unit.objects.filter(district_id=did).values()
    return JsonResponse(list(unit),safe=False)

def deletedistrict(request,district_id):
    dob = tbl_district.objects.get(district_id=district_id)
    dob.delete()
    return HttpResponse("<script>alert('District Deleted');window.location='/adminapp/viewdistrict';</script>")

def deletelocation(request,location_id):
    lob = tbl_location.objects.get(location_id=location_id)
    lob.delete()
    return HttpResponse("<script>alert('location Deleted');window.location='/adminapp/viewlocation';</script>")

def deleteunit(request,unit_id):
    uob = tbl_unit.objects.get(unit_id=unit_id)
    uob.delete()
    return HttpResponse("<script>alert('Unit Deleted');window.location='/adminapp/viewunit';</script>")

def memberreg(request):
    district = tbl_district.objects.all()
    return render(request,"admin/memberreg.html",{'district':district})

def memberreg_process(request):
    if request.method == 'POST':
        lob = Login()
        lob.username = request.POST.get("username")
        lob.password = request.POST.get("password")
        lob.role = "customer"
        lob.status = "Accepted"
        lob.save()
        mob = tbl_member()
        mob.membername = request.POST.get("membername")
        mob.memberphoto = request.FILES["memberphoto"]
        mob.licensephoto = request.FILES["licensephoto"]
        mob.membercode = request.POST.get("membercode")
        mob.memberclass = request.POST.get("class")
        mob.mobile_no = request.POST.get("phone")
        mob.email = request.POST.get("mail")
        mob.designation = request.POST.get("designation")     
        # mob.status = request.POST.get("status")
        mob.unit_id = tbl_unit.objects.get(unit_id=request.POST.get("unit"))
        mob.login_id = lob
        mob.save()
        username=request.POST.get("username")
        password=request.POST.get("password")
        Email=request.POST.get('mail')  # to address
        msg = EmailMessage()
        msg.set_content(f'You are registered to MerchCo. Try to login by using the Username: {username}, Password: {password}')
        msg['Subject'] = "Registration Completed To MerchCo"
        msg['from'] = 'ajaymanoj977@gmail.com'
        msg['To'] = {Email}
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('ajaymanoj977@gmail.com','dtgf lqaj bent slwt')
            smtp.send_message(msg)
        return HttpResponse("<script>alert(' Member Succesfully Added');window.location='/adminapp/viewmember';</script>")

def viewmember(request):
    member=tbl_member.objects.all()
    return render(request,"admin/viewmember.html",{'member':member})

def deletemember(request,memberid):
    uob = tbl_member.objects.get(member_id=memberid)
    uob.delete()
    return HttpResponse("<script>alert('Member Deleted');window.location='/adminapp/viewmember';</script>")


def welfarereg(request):
    return render(request,"admin/welfarereg.html")

def welfare_process(request):
    if request.method == 'POST':
        wob = tbl_welfare()
        wob.welfaretitle = request.POST.get("welfaretitle")
        wob.welfarepurpose = request.POST.get("welfarepurpose")
        wob.welfaredate = request.POST.get("welfaredate")
        wob.amount = request.POST.get("amount")
        wob.creditedby = "admin"
        wob.welfarestatus = "created"
        wob.save()
        return HttpResponse("<script>alert('Succesfully Inserted');window.location='/adminapp/welfarereg';</script>")

def verification(request):
    member=tbl_member.objects.filter(login_id__status = "requested")
    return render(request,"admin/verification.html",{'member':member})

def verificationaccept(request,login_id):
    lob=Login.objects.get(login_id=login_id)
    member=tbl_member.objects.get(login_id=lob)
    mailid = member.email

    lob.status="Accepted"
    lob.save()
    msg = EmailMessage()
    msg.set_content(f'Your MerchCo registration is approved by the Admin. ')
    msg['Subject'] = "Registration Completed To MerchCo"
    msg['from'] = 'ajaymanoj977@gmail.com'
    msg['To'] = {mailid}
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('ajaymanoj977@gmail.com','dtgf lqaj bent slwt')
        smtp.send_message(msg)
    return HttpResponse("<script>alert('Accepted');window.location='/adminapp/verification';</script>")

def verificationreject(request,login_id):
    lob=Login.objects.get(login_id=login_id)
    member=tbl_member.objects.get(login_id=lob)
    mailid = member.email
    lob.status="Rejected"
    lob.save()
    msg = EmailMessage()
    msg.set_content(f'Your MerchCo registration is rejected by the Admin. ')
    msg['Subject'] = "Registration Rejected To MerchCo"
    msg['from'] = 'ajaymanoj977@gmail.com'
    msg['To'] = {mailid}
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('ajaymanoj977@gmail.com','dtgf lqaj bent slwt')
        smtp.send_message(msg)
    return HttpResponse("<script>alert('Rejected');window.location='/adminapp/verification';</script>")

def notification(request):
    return render(request,"admin/notification.html")

def loanverification(request):
    loan=tbl_loan.objects.filter(loanstatus ="requested")
    return render(request,"admin/loanverification.html",{'loan':loan})

from django.utils import timezone
def loanverificationaccept(request,id):
    lob=tbl_loan.objects.get(loan_id=id)
    mail=tbl_member.objects.get(member_id=lob.member_id_id).email
    member=tbl_member.objects.get(member_id=lob.member_id_id).membername
    loan = lob.amount
    interest = lob.monthlyinterest
    installment = lob.installmentmonths
    lob.loanstatus="Accepted"
    lob.approveddate=timezone.now()
    lob.save()
    msg = EmailMessage()
    msg.set_content(f'''Dear {member},

    We are excited to inform you that your loan application has been approved! 🎉

Here are the details:
- Loan Amount: {loan}
- Interest Rate: {interest}%
- Repayment Period: {installment} months

Our team will contact you soon with next steps. If you have any questions, feel free to reach out.

Thank you for choosing MerchCo.

Best regards,  
        MerchCo''')

    msg['Subject'] = "Great News! Your Loan Application Has Been Approved 🎉"
    msg['from'] = 'ajaymanoj977@gmail.com'
    msg['To'] = {mail}
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('ajaymanoj977@gmail.com','dtgf lqaj bent slwt')
        smtp.send_message(msg)
    return HttpResponse("<script>alert('Accepted');window.location='/adminapp/loanverification';</script>")

def loanverificationreject(request,id):
    lob=tbl_loan.objects.get(loan_id=id)
    mail=tbl_member.objects.get(member_id=lob.member_id_id).email
    member=tbl_member.objects.get(member_id=lob.member_id_id).membername
    loan=lob.amount
    lob.loanstatus="Rejected"
    lob.save()
    msg = EmailMessage()
    msg.set_content(f'''Dear {member},

We regret to inform you that we are unable to approve your loan application for {loan} at this time.

If you have any questions or would like more details, feel free to contact us.

Thank you for considering MerchCo. We appreciate your understanding.

Best regards,  
MerchCo''')
    msg['Subject'] = "Update on Your Loan Application"
    msg['from'] = 'ajaymanoj977@gmail.com'
    msg['To'] = {mail}
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('ajaymanoj977@gmail.com','dtgf lqaj bent slwt')
        smtp.send_message(msg)
    return HttpResponse("<script>alert('Loan Rejected');window.location='/adminapp/loanverification';</script>")

def acceptedloan(request):
    loan=tbl_loan.objects.filter(loanstatus = "accepted")
    return render(request,"admin/acceptedloan.html",{'loan':loan})

def notification_process(request):
    if request.method == 'POST':
        wob = tbl_notification()
        wob.notificationtitle = request.POST.get("title")
        wob.notificationdescription = request.POST.get("description")
        wob.data = request.POST.get("data")
        wob.expirydate = request.POST.get("date")
        wob.notificationstatus = "created"
        wob.save()
        return HttpResponse("<script>alert('Succesfully Inserted');window.location='/adminapp/viewnotification/';</script>")

def viewwelfare(request):
    welfare=tbl_welfare.objects.filter(welfarestatus = "created")
    return render(request,"admin/viewwelfare.html",{'welfare':welfare})

def publishwelfare(request,id):
    request.session['welfareid']=id
    districts = tbl_district.objects.all()
    welfare = tbl_welfare.objects.get(welfare_id=id)
    return render(request, "admin/publishwelfare.html", {'districts': districts,'welfare':welfare})

def fill_members(request):
    sid = int(request.POST.get('sid'))
    members = tbl_member.objects.filter(unit_id=sid).values('membername', 'email', 'designation', 'memberphoto', 'member_id')  # Include memberphoto
    return JsonResponse(list(members), safe=False)

def publish_process(request):
    if request.method == "POST":
        members = request.POST.getlist("selected_members[]")
        welfare_id = request.POST.get("welfare_id")
        for p in members:
            member = tbl_member.objects.get(member_id=p)
            sob = tbl_welfarepublish()
            sob.welfare_id=tbl_welfare.objects.get(welfare_id=welfare_id)
            sob.member_id = member
            sob.save()
            lob = tbl_welfare.objects.get(welfare_id=welfare_id)
            lob.welfarestatus = "published"
            lob.save()

        return HttpResponse("<script>alert('Successfully Inserted'); window.location='/adminapp/viewwelfare';</script>")

def inactive_welfare(request,id):
    lob = tbl_welfare.objects.get(welfare_id=id)
    lob.welfarestatus = "inactivated"
    lob.save()
    return HttpResponse("<script>alert('Welfare Inactivated');window.location='/adminapp/publishedwelfare/';</script>")

def editdistrict(request,district_id):
    if request.method == 'POST':
        districtname = request.POST.get("districtname")
        dob = tbl_district.objects.get(district_id=district_id)
        dob.districtname = districtname
        dob.save()
        return HttpResponse("<script>alert('Successfully Updated..');window.location='/adminapp/viewdistrict';</script>")
    else:
        district = tbl_district.objects.get(district_id=district_id)
        return render(request,"admin/editdistrict.html",{'district':district})

def editlocation(request,location_id):
    if request.method == 'POST':
        locationname = request.POST.get("locationname")
        district_id = request.POST.get("district_id")
        lob = tbl_location.objects.get(location_id=location_id)
        lob.locationname = locationname
        lob.district_id = tbl_district.objects.get(district_id=district_id)
        lob.save()
        return HttpResponse("<script>alert('Successfully Updated..');window.location='/adminapp/viewlocation';</script>")
    else:
        location = tbl_location.objects.get(location_id=location_id)
        district = tbl_district.objects.all()
        return render(request,"admin/editlocation.html",{'location':location,'district':district    })

def editunit(request,unit_id):
    if request.method == 'POST':
        unitname = request.POST.get("unitname")
        district_id = request.POST.get("district_id")
        uob = tbl_unit.objects.get(unit_id=unit_id)
        uob.unitname = unitname
        uob.district_id = tbl_district.objects.get(district_id=district_id)
        uob.save()
        return HttpResponse("<script>alert('Successfully Updated..');window.location='/adminapp/viewunit';</script>")
    else:
        unit = tbl_unit.objects.get(unit_id=unit_id)
        district = tbl_district.objects.all()
        return render(request,"admin/editunit.html",{'unit':unit,'district':district    })

def viewloanpayment(request):
    loan = tbl_loantransaction.objects.all()

    # Get filter parameters from request
    member_id = request.GET.get('member_id')
    installment_month = request.GET.get('installment_month')
    selected_month = request.GET.get('month')  # Get selected month

    # Apply filters if parameters exist
    if member_id:
        # Assuming loan_id is a ForeignKey to another model (e.g., Loan), and Loan has a member_id field
        loan = loan.filter(loan_id__member_id=member_id)
    if installment_month:
        loan = loan.filter(loan_id__installmentmonths=installment_month)
    if selected_month:
        loan = loan.filter(paiddate__month=selected_month)  # Filter by month from paid date

    return render(request, "admin/viewloanpayment.html", {'loan': loan, 'selected_month': selected_month})


import sqlite3
from django.shortcuts import render

def dashboard(request):
    # Connect to SQLite database (or use your actual Django ORM model)
    conn = sqlite3.connect('merchco.db')
    cursor = conn.cursor()

    # Query to calculate the sum of the 'deposit' column
    cursor.execute("SELECT SUM (deposite) FROM tbl_deposite")

    # Fetch the result
    deposit_sum = cursor.fetchone()[0]

    # If no deposits exist, the sum will be None
    if deposit_sum is None:
        deposit_sum = 0

    # Close the connection
    conn.close()

    # Pass the deposit sum to the template
    return render(request, 'admin/dashboard.html', {'deposit_sum': deposit_sum})

def edit_welfare(request, welfare_id):
    if request.method == 'POST':
        welfaretitle = request.POST.get("welfaretitle")
        welfarepurpose = request.POST.get("welfarepurpose")
        welfaredate = request.POST.get("welfaredate")  # This will be empty if not changed
        amount = request.POST.get("amount")
        
        # Get the existing welfare object
        dob = tbl_welfare.objects.get(welfare_id=welfare_id)
        
        # Update the other fields
        dob.welfaretitle = welfaretitle
        dob.welfarepurpose = welfarepurpose
        dob.amount = amount
        
        # Only update the welfare date if it's provided (meaning it was changed)
        if welfaredate:
            dob.welfaredate = welfaredate

        # Save the updated object
        dob.save()
        
        # Success message and redirect
        return HttpResponse("<script>alert('Successfully Updated..');window.location='/adminapp/index/';</script>")

    else:
        # When the form is being loaded (GET request)
        welfare = tbl_welfare.objects.get(welfare_id=welfare_id)
        return render(request, "admin/edit_welfare.html", {'welfare': welfare})
    
def viewnotification(request):
    notification=tbl_notification.objects.filter(notificationstatus = "created")
    return render(request,"admin/viewnotification.html",{'notification':notification})

def inactive_notification(request,id):
    lob = tbl_notification.objects.get(notification_id=id)
    lob.notificationstatus = "cancelled"
    lob.save()
    return HttpResponse("<script>alert('Notification Inactivated');window.location='/adminapp/viewnotification';</script>")

def edit_notification(request,notification_id):
    if request.method == 'POST':
        notificationtitle = request.POST.get("title")
        notificationdescription = request.POST.get("description")
        expirydate = request.POST.get("date")
        dob = tbl_notification.objects.get(notification_id=notification_id)
        dob.notificationtitle = notificationtitle
        dob.notificationdescription = notificationdescription
        dob.expirydate = expirydate
        dob.save()
        return HttpResponse("<script>alert('Successfully Updated..');window.location='/adminapp/viewnotification';</script>")
    else:
        notification = tbl_notification.objects.get(notification_id=notification_id)
        return render(request,"admin/edit_notification.html",{'notification':notification})
    
def pie_chart(request):
    labels = []
    data = []

    queryset = tbl_unit.objects.values('district_id__districtname').annotate(total_unit=Count('unit_id'))
    for s in queryset:
        labels.append(s['district_id__districtname'])
        data.append(s['total_unit'])

    return render(request, 'admin/piechartunitdistrict.html', {
        'labels': labels,
        'data': data,
    })

class ExportExcelLoan(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="loanlist.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')

        # Define the column headings
        row_num = 0
        columns = ['Member Name','Member ID', 'Amount', 'Monthly Amount', 'Monthly Interest', 'Installment Months' ,'status','Approved Date', 'Balance Amount']
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)

        # Query the data from your model, and write it to the worksheet
        queryset = tbl_loan.objects.select_related('member_id').values_list('member_id__membername', 'member_id',  'amount', 'monthlyamount', 'monthlyinterest', 'installmentmonths','loanstatus',  'approveddate', 'balanceamount')
        # return HttpResponse(queryset)
        for row in queryset:
            row_num += 1
            for col_num, cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response
    
class ExportExcelLoantransaction(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="loanpaymentlist.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')

        # Define the column headings
        row_num = 0
        columns = ['Transaction ID','Loan ID','Member Name','Member ID', 'Amount', 'Paid Amount', 'Paid Date', 'Installment Months' ]
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)

        # Query the data from your model, and write it to the worksheet
        queryset = tbl_loantransaction.objects.select_related('loan_id').values_list('loantrans_id','loan_id','loan_id__member_id__membername', 'loan_id__member_id',  'loanamount', 'amount', 'paiddate', 'loan_id__installmentmonths')
        # return HttpResponse(queryset)
        for row in queryset:
            row_num += 1
            for col_num, cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response
    
from django.shortcuts import render


def member_details_view(request):
    # Fetch all members
    members = tbl_member.objects.all()

    # Count the A class and C class members
    a_class_count = members.filter(designation='A class').count()
    c_class_count = members.filter(designation='C class').count()

    # Context data passed to the template
    context = {
        'member': members,
        'a_class_count': a_class_count,
        'c_class_count': c_class_count,
    }

    return render(request, 'admin/member_details.html', context)

import matplotlib.pyplot as plt
from io import BytesIO
from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.http import HttpResponse
import calendar


def deposit_bar_chart(request):
    # Get the current year
    current_year = datetime.now().year
    
    # Create a list of all months (1 to 12)
    months_list = list(range(1, 13))

    # Aggregate the deposits by month (use year and month only, no need for datetime)
    total_deposits = tbl_deposite.objects.annotate(month=TruncMonth('depositedate')) \
                                        .values('month') \
                                        .annotate(total_deposit=Sum('deposite')) \
                                        .order_by('month')

    # Prepare the data for plotting
    month_labels = [calendar.month_name[m] for m in months_list]  # Get month names (e.g., "January", "February", etc.)
    totals = [0] * 12  # Initialize a list with 0 values for each month

    # Populate the totals list with actual deposit values for each month
    for entry in total_deposits:
        month_index = entry['month'].month - 1  # Get the index of the month (0-based)
        totals[month_index] = entry['total_deposit']

    # Create the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(month_labels, totals, color='blue')

    # Add labels and title
    plt.xlabel('Month')
    plt.ylabel('Total Deposit')
    plt.title(f'Total Deposits per Month for {current_year}')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the figure to a BytesIO object (in-memory image)
    img_io = BytesIO()
    plt.savefig(img_io, format='png')
    img_io.seek(0)  # Seek to the beginning of the BytesIO object

    # Return the image as HTTP response
    return HttpResponse(img_io, content_type='image/png')

import matplotlib.pyplot as plt
from io import BytesIO
from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.http import HttpResponse
import calendar
from datetime import datetime

def loan_transaction_area_chart(request):
    # Get the current year
    current_year = datetime.now().year

    # Create a list of all months (1 to 12)
    months_list = list(range(1, 13))

    # Aggregate the loan transaction amounts by month (use paiddate field)
    total_amounts = tbl_loantransaction.objects.annotate(month=TruncMonth('paiddate')) \
                                               .values('month') \
                                               .annotate(total_amount=Sum('amount')) \
                                               .order_by('month')

    # Prepare the data for plotting
    month_labels = [calendar.month_name[m] for m in months_list]  # Get month names (e.g., "January", "February", etc.)
    totals = [0] * 12  # Initialize a list with 0 values for each month

    # Populate the totals list with actual transaction amounts for each month
    for entry in total_amounts:
        month_index = entry['month'].month - 1  # Get the index of the month (0-based)
        totals[month_index] = entry['total_amount']

    # Create the area graph
    plt.figure(figsize=(10, 6))
    plt.fill_between(month_labels, totals, color='skyblue', alpha=0.4)  # Area graph with a fill
    plt.plot(month_labels, totals, color='blue', marker='o', linestyle='-', linewidth=2)  # Outline the area

    # Annotate each point with the total amount
    for i, total in enumerate(totals):
        if total > 0:  # Only annotate non-zero values
            plt.text(month_labels[i], total + 0.5, f'{total:.2f}', ha='center', va='bottom', fontsize=9)

    # Add labels and title
    plt.xlabel('Month')
    plt.ylabel('Total Amount Paid')
    plt.title(f'Total Loan Amount Paid per Month for {current_year}')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the figure to a BytesIO object (in-memory image)
    img_io = BytesIO()
    plt.savefig(img_io, format='png')
    img_io.seek(0)  # Seek to the beginning of the BytesIO object

    # Return the image as HTTP response
    return HttpResponse(img_io, content_type='image/png')

def publishedwelfare(request):
    welfare1=tbl_welfare.objects.filter(welfarestatus = "published")
    return render(request,"admin/publishedwelfare.html",{'welfare':welfare1})

def viewwelfarepayment(request):
    welfare = tbl_welfaretransaction.objects.all()

    # Get filter parameters from request
    member_id = request.GET.get('member_id')
    selected_month = request.GET.get('month')  # Get selected month

    # Apply filters if parameters exist
    if member_id:
        # Assuming loan_id is a ForeignKey to another model (e.g., Loan), and Loan has a member_id field
        welfare = welfare.filter(member_id=member_id)
    if selected_month:
        welfare = welfare.filter(date__month=selected_month)  # Filter by month from paid date

    return render(request, "admin/viewwelfarepayment.html", {'welfare': welfare, 'selected_month': selected_month})

from django.db.models import Sum


def total_deposit_view(request):
    # Calculate the total of the 'deposite' field
    total_deposit = tbl_deposite.objects.aggregate(total=Sum('deposite'))['total']

    # If there are no deposits, set the total to 0
    if total_deposit is None:
        total_deposit = 0
    
    # Print total deposit to console for debugging
    print(f"Total Deposit: {total_deposit}")

    # Pass the total_deposit to the template
    return render(request, 'your_template.html', {'total_deposit': total_deposit})




