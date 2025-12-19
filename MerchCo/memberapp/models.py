from django.db import models
from adminapp.models import tbl_member,tbl_welfare

# Create your models here.
class tbl_deposite(models.Model):
    deposite_id = models.AutoField(primary_key=True)  
    member_id = models.ForeignKey(tbl_member,on_delete=models.CASCADE)  
    depositedate = models.DateField(auto_now_add=True) 
    deposite = models.FloatField()
    matureddate = models.DateField(null=True)  
    interestrate = models.FloatField(null=True)
    matuedamount = models.FloatField(null=True) 
    
class tbl_loan(models.Model):
    loan_id = models.AutoField(primary_key=True)  
    member_id = models.ForeignKey(tbl_member,on_delete=models.CASCADE)  
    date = models.DateField(auto_now_add=True) 
    approveddate=models.DateField(null=True)
    installmentmonths = models.IntegerField(default=0)
    amount = models.FloatField()  
    balanceamount = models.FloatField(null=True)  
    monthlyinterest = models.FloatField()
    monthlyamount = models.FloatField() 
    loanstatus = models.CharField(max_length=20)

class tbl_welfaretransaction(models.Model):
    trans_id = models.AutoField(primary_key=True)  
    member_id = models.ForeignKey(tbl_member,on_delete=models.CASCADE)  
    welfare_id = models.ForeignKey(tbl_welfare,on_delete=models.CASCADE)  
    date = models.DateField(auto_now_add=True) 
    welfareamount = models.FloatField() 

class tbl_loantransaction(models.Model):
    loantrans_id = models.AutoField(primary_key=True)  
    loan_id = models.ForeignKey(tbl_loan,on_delete=models.CASCADE)   
    paiddate = models.DateField(auto_now_add=True) 
    loanamount = models.FloatField()  
    amount = models.FloatField() 
    fine=models.IntegerField(null=True)
    paidduedate=models.DateField(null=True)
    status = models.CharField(max_length=20,null=True)
    
    
