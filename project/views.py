from project.models import *
from django.shortcuts import render_to_response, redirect, get_object_or_404
from project.forms import *
from project.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from django.core.files.storage import default_storage
from django.conf import settings
from django.utils import timezone
import os
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
import re

from django.views.static import serve
from datetime import timedelta
from django.shortcuts import render


# Create your views here.
def loginuser(request):
	message=" "
	p=UserForm()
	if request.method=="POST":                
		p=UserForm(request.POST)
                uname = request.POST['username']
                password = request.POST['password']

                user=authenticate(username=uname,password=password)
                if user is not None:
			if user.is_staff:
				login(request,user)
				return HttpResponseRedirect('/doct1/')
	
			login(request,user)
			print request.user
			return HttpResponseRedirect('/home/')
                else:
                        message="Invalid username or password"
                        return render_to_response('Login.htm',{"p":p, "message":message},context_instance=RequestContext(request))
        else:
                return render_to_response('Login.htm',{"p":p, "message":message},context_instance=RequestContext(request))
	

def signup(request):
        message=""
        if request.method=="POST":
                p=UserForm(request.POST)
                if p.is_valid():
                        username = request.POST["username"]
                        print username
                        u = User.objects.all().filter(username=request.POST['username'])
                        if len(u) == 0 :
                                u = User.objects.create_user(request.POST['username'],password=request.POST['password'])
                                u.first_name=request.POST['first_name']
                                u.last_name=request.POST['last_name']
				a=request.POST['docorpat']
				print " A is " + a
				if a == 'doc' :
					print "In staff section"
					u.is_staff=True
					#print u.is_staff=True
					 
                                l = log()
				j=symptoms()
				k=doc()
                                try:
                                        u.save()
				#	print u.is_staff==True
					                                        
					l.user = u
                                        l.save()
					j.user=u
					j.done=0
					j.save()
					k.user=u
					k.save()
                                        message="Username is Successfully stored in Database"
					login(request,u)
                                        return HttpResponseRedirect('/home/')			
                                except ValueError:
                                        message="Something is not right..Check your Sign Up Form"
					print "huib"                                        
					return HttpResponseRedirect('/signup/')			
                                        #u.delete()
			else:
				message="Username Already Exist... Please select another ....!!!"
                        	return render_to_response('Signup.htm',{"p":p, "message":message},context_instance=RequestContext(request))			
                        
                else:
                        message="Something is not right..Check your Sign Up Form"
                        return render_to_response('Signup.htm',{"p":p, "message":message},context_instance=RequestContext(request))			
                                        
                        
        else:
                p=UserForm()
                return render_to_response('Signup.htm',{"p":p, "message":message},context_instance=RequestContext(request))



# Create your views here.
def home(request):
	try:
		p=User.objects.get(username=request.user.username)
		print p.first_name
		message="Login Successful! "
		#var1 = welcome_page.objects.all()
		return render_to_response('homepage.html',{"p":p,"message":message})#,context_instance=RequestContext(request))
	except:	
		return render_to_response('homepage1.html')#,context_instance=RequestContext(request))
		
@login_required
def update(request):
	p=UpdateForm()
	if request.user.is_authenticated:
		if request.method=="POST":
			p=UpdateForm(request.POST)
			ua = User.objects.get(username=request.user.username)
			if ua is not None :
				print ua
				print request.user
				print request.user.id
				cust_user = log.objects.get(user=request.user)
				cust_user.add=request.POST['add']
				#cust_user.dob=p.request.POST['dob']
				cust_user.bgrp=request.POST['bgrp']
				cust_user.gender=request.POST['gen']
				cust_user.city=request.POST['city']
				cust_user.occupation=request.POST['occupation']
				cust_user.save()
				ua=User.objects.get(id=request.user.id)
				ua.first_name=request.POST['first_name']
				ua.last_name=request.POST['last_name']
				ua.email=request.POST['email']
				ua.save()
				message="Data Updated Successfully ! "
				return render_to_response('profile.htm',{"p":p,"message":message},context_instance=RequestContext(request))
			else:
				message="User Not Found"
				return render_to_response('profile.htm',{"p":p,"message":message},context_instance=RequestContext(request))
		else:
			return render_to_response('profile.htm',{"p":p},context_instance=RequestContext(request))
	#var1 = welcome_page.objects.all()
	return render_to_response('homepage.html',)

@login_required
def sympt(request):
	p=SymptomsForm()
	if request.user.is_authenticated:
		if request.method=="POST":
			p=SymptomsForm(request.POST)
			ua = User.objects.get(username=request.user.username)
			if ua is not None :
				print ua
				print request.user
				print request.user.id
				cust_user = symptoms.objects.get(user=request.user)
				cust_user.symp=request.POST['symp']
				cust_user.duration=request.POST['duration']
				cust_user.intensity=request.POST['intensity']
				cust_user.relsymp=request.POST['relsymp']
				cust_user.history=request.POST['history']
				cust_user.treat=request.POST['treat']
				cust_user.diag=request.POST['diag']
				cust_user.premed=request.POST['premed']
				cust_user.diab=request.POST['diab']
				cust_user.hab=request.POST['hab']
				cust_user.bp=request.POST['bp']
				cust_user.smokhab=request.POST['smokhab']
				cust_user.weight=request.POST['weight']
				cust_user.height=request.POST['height']
				cust_user.done=1
				cust_user.save()
				message="Your Symptoms Form is successfully registered "
				return render_to_response('patpage.htm',{"p":p,"message":message},context_instance=RequestContext(request))
			else:
				message="User Not Found"
				return render_to_response('login.htm',{"p":p,"message":message},context_instance=RequestContext(request))
		else:
			return render_to_response('patpage.htm',{"p":p},context_instance=RequestContext(request))
	#var1 = welcome_page.objects.all()
	return render_to_response('homepage.html',)
			

@login_required
def doct1(request):
	print "Hello"
	if request.method=="POST":
		p=request.POST['pat']		
		print p
		q1= User.objects.get(username=p)
		print q1.username ,q1.first_name
		p= symptoms.objects.get(user=q1)
		q=log.objects.get(user=q1)
		
		print p.symp,p.bp
		
		return render_to_response('docview.htm',{"p":p,"q":q,"q1":q1},context_instance=RequestContext(request))
	else:
		#q=SelectpatForm()
		#q=symptoms.objects.filter(done=0)		
		p1=User.objects.exclude(is_staff=1)
				
		#p=symptoms.objects.all().filter(user=p1)
		#print p[0]
		#print q
		return render_to_response('selectpat.htm',{"p":p1},context_instance=RequestContext(request))
									
def docres(request):
	if request.method=="POST":
		name=request.POST['name']
		u1= User.objects.get(first_name=name)
		u=doc.objects.get(user=u1)
		u.pres=request.POST['pres']
		u.advice=request.POST['advice']
		u.prec=request.POST['prec']
		u.save()	
		return HttpResponseRedirect('/doct1/')			
                                        
	else:
		p=DoctorResponseForm()
		return render_to_response('DocResponse.htm',{"p":p},context_instance=RequestContext(request))
def patget(request):
	u=User.objects.get(username=request.user.username)
	u1=doc.objects.get(user=request.user)	
	print u1.prec
	print u1.user
		
	return render_to_response('patview.htm',{"p":u1},context_instance=RequestContext(request))
def about(request):
	return render_to_response('About.htm',)
def children(request):
	if request.method=="POST" :
			u=User.objects.get(username=request.user.username)
			cust=symptoms.objects.get(user=u)	
			cust.head=request.POST.get('head','No')
			cust.fever=request.POST.get('fever','No')
			cust.sad=request.POST.get('sad','No')
			print "Hello"
			cust.save()
		        return HttpResponseRedirect('/children1/')
		#else:
		#	return HttpResponseRedirect('/children/')			
	else:
		return render_to_response('children.htm',context_instance=RequestContext(request))
		
def children1(request):
	if request.method=="POST" :
			u=User.objects.get(username=request.user.username)
			cust=doc.objects.get(user=u)	
			cust.stomach=request.POST.get('st','No')
			cust.flu=request.POST.get('flu','No')
			cust.itching=request.POST.get('itching','No')
			cust.save()
			return HttpResponseRedirect('/child/')
	else:
		return render_to_response('children1.htm',context_instance=RequestContext(request))
def child(request):
	if request.method=="POST" :
		#if Yes in request.POST:	
		print "Hello"	
		p=symptoms.objects.get(user=request.user)
				
		p.add=request.POST['add']
		p.save()
		return HttpResponseRedirect('/home/')
		#else:
		#	return HttpResponseRedirect('/children/')
	else:
		p=symptoms.objects.get(user=request.user)			
		return render_to_response('child_verify.htm',{"p":p},context_instance=RequestContext(request))
		
					



def contact(request):
    return render_to_response('Contact.htm',)
