from django.shortcuts import render,redirect
from guestapp.models import Login
from memberapp.models import tbl_deposite
from adminapp.models import tbl_district,tbl_unit,tbl_member
from django.http import HttpResponse,JsonResponse

# Create your views here.
def login(request):
    return render(request,"guest/login.html")

def loginprocess(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Check if the username and password match a login object
        if Login.objects.filter(username=username, password=password).exists():
            loginobj = Login.objects.get(username=username, password=password)
            request.session['loginid'] = loginobj.login_id
            role = loginobj.role
            
            if role == "admin":
                return redirect('/adminapp/index/')
            elif role == "customer":
                if loginobj.status == 'Accepted':
                    # Obtain member_id corresponding to loginobj from tbl_member
                    try:
                        member = tbl_member.objects.get(login_id=loginobj.login_id)  # Assuming login_id is a foreign key to tbl_member
                        member_id = member.member_id  # Get the member_id from tbl_member
                        
                        # Check if the member_id exists in the tbl_deposit table
                        if tbl_deposite.objects.filter(member_id=member_id).exists():
                            return redirect('/memberapp/index/')  # Redirect to member index if deposit exists
                        else:
                            return redirect('registerfeepayment',member_id=member_id)  # Redirect to payment form if no deposit record
                    except tbl_member.DoesNotExist:
                        return HttpResponse("<script>alert('Member record not found.');window.location='/guestapp/login';</script>")
                else:
                    return HttpResponse("<script>alert('Request not Accepted');window.location='/guestapp/login';</script>")
            else:
                return HttpResponse("<script>alert('Not an authorized person');window.location='/guestapp/login';</script>")
        else:
            return HttpResponse("<script>alert('Invalid username or password');window.location='/guestapp/login';</script>")


def index(request):
    return render(request,"guest/index.html")

def register(request):
    district = tbl_district.objects.all()
    return render(request,"guest/register.html",{'district':district})

def register_process(request):
    if request.method == 'POST':
        lob = Login()
        lob.username = request.POST.get("username")
        lob.password = request.POST.get("password")
        lob.role = "customer"
        lob.status = "requested"
        lob.save()
        mob = tbl_member()
        mob.membername = request.POST.get("membername")
        mob.memberphoto = request.FILES.get("memberphotos")
        mob.licensephoto = request.FILES.get("licensephotos")
        mob.membercode = request.POST.get("membercode")
        mob.memberclass = request.POST.get("class")
        mob.mobile_no = request.POST.get("phone")
        mob.email = request.POST.get("mail")
        mob.designation = request.POST.get("designation")
        # mob.status = request.POST.get("status")
        mob.unit_id = tbl_unit.objects.get(unit_id=request.POST.get("unit"))
        mob.login_id = lob
        mob.save()
        return HttpResponse("<script>alert('Your Request is sent. You will be approved later.');window.location='/';</script>")
    
from django.shortcuts import get_object_or_404
from django.utils import timezone

def registerfeepayment(request, member_id):
    # Retrieve the member record
    member = get_object_or_404(tbl_member, pk=member_id)

    # Determine the payment amount based on the member's class
    amount_mapping = {
        'A-Class': 5000,
        'C-Class': 1000
    }
    amount = request.POST.get('amount')

    if request.method == "POST":
        # Insert into the tbl_deposite table
        tbl_deposite.objects.create(
            member_id=member,  # ForeignKey reference
            depositedate=timezone.now().date(),
            deposite=amount
        )

        return HttpResponse("<script>alert('Payment Successful!');window.location='/memberapp/index/';</script>")

    # Prepare context for the template
    context = {
        'member_id': member_id,
        'amount': amount,
        'memberclass': member.memberclass,
        'name': member.membername,
    }

    return render(request, "guest/registerfeepayment.html",context)