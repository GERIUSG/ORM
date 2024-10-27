from django.db import models
from django.contrib import admin
class bankloan (models.Model):
    Name=models.CharField(max_length=20)
    accno=models.CharField(max_length=20,primary_key=True)
    loanid=models.IntegerField()
    amount=models.IntegerField()
    ifsccode=models.CharField(max_length=11)

class bankloanAdmin(admin.ModelAdmin):
        list_display=('Name','accno','loanid','amount','ifsccode')