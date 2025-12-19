from django.shortcuts import get_object_or_404, render, redirect
from adminapp import models
from adminapp.models import tbl_district,tbl_unit,tbl_member,tbl_welfarepublish,tbl_welfare,tbl_notification
from guestapp.models import Login
from memberapp.models import tbl_deposite,tbl_loan,tbl_welfaretransaction,tbl_loantransaction
from django.http import HttpResponse,JsonResponse
from datetime import datetime, timedelta
from django.utils import timezone
from django.views.decorators.cache import cache_control
from django.db.models import Sum, Count
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def index(request):
    logid = request.session.get('loginid')
    
    if logid:
        try:
            # Retrieve the member based on the login_id
            member = tbl_member.objects.get(login_id=logid)
            notification = tbl_notification.objects.all()
            # Get the total deposit for the corresponding member
            total_deposit = tbl_deposite.objects.filter(member_id=member.member_id).aggregate(total=Sum('deposite'))['total']
            
            # If there are no deposits, set the total to 0
            total_deposit = total_deposit if total_deposit else 0
            
            # Get the count of loans for the corresponding member
            loan_count = tbl_loan.objects.filter(member_id=member.member_id).count()
            
            # Get the paid loan transactions for the corresponding member
            loan_transactions = tbl_loantransaction.objects.filter(loan_id__member_id=member.member_id, status="paid")
             
            # Pass the total deposit, loan count, and loan transactions to the template
            return render(request, "member/index.html", {
                'total_deposit': total_deposit, 
                'loan_count': loan_count,
                'loan_transactions': loan_transactions,
                'member' : member,
                'notification' : notification,
            })
        
        except tbl_member.DoesNotExist:
            return HttpResponse("<script>alert('Member not found.');window.location='/login';</script>")
    
    else:
        return HttpResponse("<script>alert('Authentication required. Please login first..');window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deposite(request):
    logid = request.session.get('loginid')
    if logid:
        member = tbl_member.objects.all()
        return render(request,"member/deposite.html",{'member':member})
    else:
        return HttpResponse("<script>alert('Authentifiction required. Please login first..');window.location='/login';</script>")
    



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deposite_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == 'POST':
            mid = tbl_member.objects.get(login_id=request.session['loginid'])
            mob = tbl_deposite()
            mob.deposite = request.POST.get("deposite")
            mob.matureddate = request.POST.get("mdate")
            mob.interestrate = request.POST.get("interestrate")
            mob.matuedamount = request.POST.get("mamount")
            mob.member_id =mid
            mob.save()
            return HttpResponse("<script>alert(' Deposited Succesfully');window.location='/memberapp/deposite';</script>")
    else:
        return HttpResponse("<script>alert('Authentifiction required. Please login first..');window.location='/login';</script>")    

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loanreq(request):
    logid = request.session.get('loginid')
    if logid:
        return render(request,"member/loanreq.html")
    else:
        return HttpResponse("<script>alert('Authentifiction required. Please login first..');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loanreq_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == 'POST':
            mid = tbl_member.objects.get(login_id=request.session['loginid'])
            lob = tbl_loan()
            lob.amount = request.POST.get("amount")
            lob.balanceamount = request.POST.get("amount")
            lob.monthlyinterest = request.POST.get("minterest")
            lob.monthlyamount = request.POST.get("monthlyamount")
            lob.installmentmonths = request.POST.get("years")
            lob.loanstatus = "requested"
            lob.member_id =mid
            lob.save()
            return HttpResponse("<script>alert('Loan Requested');window.location='/memberapp/loanreq';</script>")
    else:
        return HttpResponse("<script>alert('Authentifiction required. Please login first..');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def welfareview(request):
    logid = request.session.get('loginid')
    if logid:
        member=tbl_member.objects.get(login_id=request.session['loginid'])
        welfare=tbl_welfarepublish.objects.filter(member_id=member,welfare_id__welfarestatus="published")
        return render(request,"member/welfareview.html",{'welfare':welfare})
    else:
        return HttpResponse("<script>alert('Authentifiction required. Please login first..');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def welfarepayment(request,id):
    logid = request.session.get('loginid')
    if logid:
        request.session['welfarepublish_id']=id
        welfare=tbl_welfarepublish.objects.get(welfarepublish_id=id)
        return render(request,"member/welfarepayment.html",{'welfare':welfare})
    else:
        return HttpResponse("<script>alert('Authentifiction required. Please login first..');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def payment_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method== 'POST':
            member = request.POST.get("member")
            welfareid = request.POST.get("welfareid")
            amount=request.POST.get("amount")
            member=tbl_member.objects.get(login_id=request.session['loginid'])
            mob = tbl_welfaretransaction()
            mob.welfare_id=tbl_welfare.objects.get(welfare_id=welfareid)
            mob.member_id = member
            mob.welfareamount = amount
            mob.save()
            return HttpResponse("<script>alert('Loan Requested');window.location='/memberapp/welfareview';</script>")

        return render(request,"member/welfarepayment.html")
    else:
        return HttpResponse("<script>alert('Authentifiction required. Please login first..');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)    
def notificationview(request):
    logid = request.session.get('loginid')
    if logid:
        notification=tbl_notification.objects.filter(notificationstatus="created")
        return render(request,"member/notificationview.html",{'notification':notification})
    else:
        return HttpResponse("<script>alert('Authentifiction required. Please login first..');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewloanreq(request):
    logid = request.session.get('loginid')
    if logid:
        member=tbl_member.objects.get(login_id=request.session['loginid'])
        loan=tbl_loan.objects.filter(member_id=member,loanstatus="Accepted")
        return render(request,"member/viewloanreq.html",{'loan':loan})
    else:
        return HttpResponse("<script>alert('Authentifiction required. Please login first..');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loantransaction(request, id):
    loan = tbl_loan.objects.get(loan_id=id)
    transactions = tbl_loantransaction.objects.filter(loan_id=loan, status="paid")

    if loan.loanstatus == 'Accepted' and loan.approveddate:
        approved_date = loan.approveddate
        installment_dates = []

        for i in range(loan.installmentmonths):
            transaction_date = approved_date + timedelta(days=30 * (i + 1))
            installment_dates.append(transaction_date)

        # Get all paid due dates
        paid_due_dates = list(transactions.values_list('paidduedate', flat=True))
        paid_due_dates = [date.strftime('%Y-%m-%d') for date in paid_due_dates if date]  # Format dates as string

        current_date = timezone.now().date()

        return render(request, 'member/loantransaction.html', {
            'loan': loan,
            'installment_dates': installment_dates,
            'loantrans': transactions,
            'paid_due_dates': paid_due_dates,  # Pass paid due dates to template
            'current_date': current_date
            })
            # Render the HTML template to show the dates
        return render(request, 'member/loantransaction.html', {'loan': loan,'installment_dates': installment_dates,'loantrans':transactions})
    else:
        return HttpResponse("<script>alert('Authentifiction required. Please login first..');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loanpayment(request,id):
    logid = request.session.get('loginid')
    if logid:
        request.session['loan_id']=id
        loan=tbl_loan.objects.get(loan_id=id)
        return render(request,"member/loanpayment.html",{'loan':loan})
    else:
        return HttpResponse("<script>alert('Authentifiction required. Please login first..');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loanpayment_process(request):
    if request.method == 'POST':
        monthlyamount = float(request.POST.get("monthlyamount"))
        loan_id = request.POST.get("loan")
        amount = float(request.POST.get("amount"))
        duedate_str = request.POST.get("due_date")  # Get due date as string

        # Convert due date string to datetime object
        duedate = datetime.strptime(duedate_str, "%Y-%m-%d").date()
        today = datetime.today().date()

        # Calculate fine: ₹100 per week after due date
        fine_amount = 0
        if today > duedate:
            overdue_days = (today - duedate).days
            fine_amount = (overdue_days // 7) * 100  # ₹100 per week

        loan = get_object_or_404(tbl_loan, loan_id=loan_id)

        if loan.balanceamount is None:
            loan.balanceamount = loan.amount  # Initialize balance

        # Save payment details
        transaction = tbl_loantransaction.objects.create(
            loan_id=loan,
            loanamount=amount,
            amount=monthlyamount,
            fine=fine_amount,
            status="paid",
            paidduedate=duedate
        )

        loan.balanceamount -= monthlyamount + fine_amount  # Deduct fine as well

        if loan.balanceamount <= 0:
            loan.balanceamount = 0
            loan.loanstatus = "completed"

        loan.save()

        return HttpResponse(
            "<script>alert('Loan paid successfully!'); window.location='/memberapp/viewloanreq';</script>"
        )

        return render(request, "member/loanpayment.html")
    else:
        return HttpResponse("<script>alert('Authentifiction required. Please login first..');window.location='/login';</script>")
    

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewpayments(request):
    logid = request.session.get('loginid')
    if logid:
        member=tbl_member.objects.get(login_id=request.session['loginid'])
        loan=tbl_loantransaction.objects.filter(loan_id__member_id=member,status="paid")
        return render(request,"member/viewpayments.html",{'loan':loan})
    else:
        return HttpResponse("<script>alert('Authentifiction required. Please login first..');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profile(request):
    logid = request.session.get('loginid')
    if logid: 
        member_id = tbl_member.objects.get(login_id=request.session['loginid']).member_id
        member = tbl_member.objects.get(member_id=member_id)
        return render(request, "member/profile.html", {'member':member})
    else:
        return HttpResponse("<script>alert('Authentifiction required. Please login first..');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit_member(request,member_id):
    logid = request.session.get('loginid')
    if logid:
        if request.method == 'POST':
            membername = request.POST.get("membername")
            mobile_no = request.POST.get("phone")
            email = request.POST.get("mail")
            memberphoto=request.POST.get('memberphoto')
            licensephoto=request.POST.get('licensephoto')
            dob = tbl_member.objects.get(member_id=member_id)
            dob.memberphoto = memberphoto
            if 'memberphoto' in request.FILES:
                dob.memberphoto = request.FILES["memberphoto"]
            else:
                dob.memberphoto = request.POST.get("oldimage")
            dob.licensephoto = licensephoto
            if 'licensephoto' in request.FILES:
                dob.licensephoto = request.FILES["licensephoto"]
            else:
                dob.licensephoto = request.POST.get("oldlicenseimage")
            dob.membername = membername
            dob.mobile_no = mobile_no
            dob.email = email       
            dob.save()
            return HttpResponse("<script>alert('Successfully Updated..');window.location='/memberapp/profile';</script>")
        else:
            member = tbl_member.objects.get(member_id=member_id)
            district = tbl_district.objects.all()
            return render(request,"member/edit_member.html",{'member':member,'district':district})
    else:
        return HttpResponse("<script>alert('Authentifiction required. Please login first..');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)    
def fillunit(request):
    logid = request.session.get('loginid')
    if logid:
        did = int(request.POST.get("did"))
        unit = tbl_unit.objects.filter(district_id=did).values()
        return JsonResponse(list(unit),safe=False)
    else:
        return HttpResponse("<script>alert('Authentifiction required. Please login first..');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    logid = request.session.get('loginid')
    if logid:
        request.session.clear()
        return redirect('/')
    else:
        return HttpResponse("<script>alert('Authentifiction required. Please login first..');window.location='/login';</script>")
    



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import tbl_deposite

@login_required
def dashboard(request):
    # Get the member_id from session (assuming it's stored in session after login)
    member_id = request.session.get('member_id')  # You can store this member_id in the session upon login
    
    if member_id is None:
        # Handle the case where the member_id is not found in the session (if necessary)
        return render(request, "member/index.html", {'total_deposit': 0})
    
    # Calculate the sum of deposits for the member with the given member_id
    total_deposit = tbl_deposite.objects.filter(member_id=member_id).aggregate(Sum('deposite'))['deposite__sum']
    
    return render(request, "member/index.html", {'total_deposit': total_deposit})


