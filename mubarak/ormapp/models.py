from django.db import models
from django.contrib import admin
class loanofficer(models.Model):

 

 Name=models.CharField(max_length=10)

 Age=models.IntegerField(primary_key="Age")
 Email=models.EmailField()
 DoB=models.DateField()
 loan_amount=models.IntegerField()
 interest_rate=models.FloatField()
class loanofficerAdmin(admin.ModelAdmin):
    list_display=('Name','Age','Email','DoB','loan_amount','interest_rate','typeofinterest')
 
