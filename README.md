# Ex02 Django ORM Web Application
## Date: 4-11-2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<Screenshot (41).png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py 
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
 
admin.py
from django.contrib import admin
from .models import loanofficer,loanofficerAdmin
admin.site.register(loanofficer,loanofficerAdmin)
```


## OUTPUT
![alt text](<Screenshot (40).png>)
Include the screenshot of your admin page.


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
