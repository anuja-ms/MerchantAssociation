from django.db import models
from guestapp.models import Login

# Create your models here.
class tbl_district(models.Model):
    district_id = models.AutoField(primary_key=True)
    districtname = models.CharField(max_length=50)

class tbl_location(models.Model):
    location_id = models.AutoField(primary_key=True)  
    locationname = models.CharField(max_length=50)  
    district_id = models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_unit(models.Model):
    unit_id = models.AutoField(primary_key=True)  
    unitname = models.CharField(max_length=50)  
    district_id = models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_member(models.Model):
    member_id = models.AutoField(primary_key=True)  
    membername = models.CharField(max_length=50)  
    unit_id = models.ForeignKey(tbl_unit,on_delete=models.CASCADE)
    memberphoto = models.ImageField() 
    licensephoto = models.ImageField()
    memberclass = models.CharField(max_length=50,default=0)
    mobile_no = models.BigIntegerField() 
    email = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)  
    membercode = models.IntegerField(default=0)
    login_id = models.ForeignKey(Login,on_delete=models.CASCADE)

class tbl_welfare(models.Model):
    welfare_id = models.AutoField(primary_key=True)  
    welfaretitle = models.CharField(max_length=50)  
    welfarepurpose = models.CharField(max_length=250)
    welfare = models.CharField(max_length=500)
    welfaredate = models.DateField() 
    amount = models.FloatField()
    creditedby = models.CharField(max_length=50) 
    welfarestatus = models.CharField(max_length=50)  

class tbl_notification(models.Model):
    notification_id = models.AutoField(primary_key=True)  
    notificationtitle = models.CharField(max_length=100)  
    notificationdescription = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True,null=True)
    expirydate = models.DateField()  
    notificationstatus = models.CharField(max_length=50)  
    
class tbl_welfarepublish(models.Model):
    welfarepublish_id = models.AutoField(primary_key=True)  
    member_id = models.ForeignKey(tbl_member,on_delete=models.CASCADE)
    welfare_id = models.ForeignKey(tbl_welfare,on_delete=models.CASCADE)

    