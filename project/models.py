from django.db import models
from django.contrib import admin

# Create your models here.
from django.contrib.auth.models import User, UserManager

class log(models.Model):
	user=models.OneToOneField(User)	
	add=models.CharField(max_length=500)
	#dob=models.DateTimeField()
	bgrp=models.CharField(max_length=5)
	gender=models.CharField(max_length=1)
	city=models.CharField(max_length=30)
	occupation=models.CharField(max_length=30)
	#mob=models.IntegerField(max_length=13)	
	
	
class symptoms(models.Model):
	user=models.OneToOneField(User)		
	symp=models.CharField(max_length=30)
	duration=models.CharField(max_length=30)
	intensity=models.CharField(max_length=30)
	relsymp=models.CharField(max_length=30)
	history=models.CharField(max_length=30)
	treat=models.CharField(max_length=30)
	diag=models.CharField(max_length=30)
	premed=models.CharField(max_length=30)
	diab=models.CharField(max_length=15)
	bp=models.CharField(max_length=15)
	smokhab=models.CharField(max_length=15)
	weight=models.CharField(max_length=5)
	height=models.CharField(max_length=5)
	hab=models.CharField(max_length=15)
	done=models.IntegerField()
	stomach=models.CharField(max_length=5)
	head=models.CharField(max_length=5)
	fever=models.CharField(max_length=5)
	flu=models.CharField(max_length=5)
	sad=models.CharField(max_length=5)
	itching=models.CharField(max_length=5)
	add=models.CharField(max_length=50)

class doc(models.Model):
	user=models.OneToOneField(User)			
	advice=models.CharField(max_length=50)
	prec=models.CharField(max_length=50)		
	pres=models.CharField(max_length=50)		
			


