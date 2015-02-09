from django import forms
'''
class loginform(forms.Form):
	uname=forms.CharField(max_length=30,widget=forms.TextInput())
	pd=forms.CharField(max_length=30,widget=forms.PasswordInput())
'''
class UserForm(forms.Form):
    """receiptNo = forms.IntegerField(widget=forms.TextInput(attrs={
      'placeholder': 'Receipt Number'
      }))"""
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={
      'placeholder': 'Username'
      }))
    first_name = forms.CharField(label="First Name",  widget=forms.TextInput(attrs={
      'placeholder': 'First Name'
      }))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={
      'placeholder': 'Last Name'
      }))
    password = forms.CharField(max_length=15,widget=forms.PasswordInput(attrs={
      'placeholder': 'Password'}))

class UpdateForm(forms.Form):
	email=forms.CharField(label="email", widget=forms.TextInput(attrs={
      'placeholder': 'Email'
      }))
	mob=forms.IntegerField(label="mobile", widget=forms.TextInput(attrs={
      'placeholder': 'Mobile No'
      }))
	add=forms.CharField(label="address", widget=forms.TextInput(attrs={
      'placeholder': 'Address'
      }))
	dob=forms.DateTimeField(label="dob",input_formats=('%Y-%m-%d %H:%M:%S+0530'))
	bgrp=forms.CharField(label="bgrp", widget=forms.TextInput(attrs={
      'placeholder': 'Blood Group'
      }))
	gender=forms.CharField(label="gender", widget=forms.TextInput(attrs={
      'placeholder': 'Gender'
      }))
	city=forms.CharField(label="city", widget=forms.TextInput(attrs={
      'placeholder': 'City'
      }))
	occupation=forms.CharField(label="occupation", widget=forms.TextInput(attrs={
      'placeholder': 'Occupation'
      }))
	first_name = forms.CharField(label="first_name",  widget=forms.TextInput(attrs={
      'placeholder': 'First Name'
      }))
	last_name = forms.CharField(label="last_name", widget=forms.TextInput(attrs={
      'placeholder': 'Last Name'
      }))

class SymptomsForm(forms.Form):
	symp=forms.CharField(label="symp", widget=forms.TextInput(attrs={
      'placeholder': 'Symptoms'
      }))
	duration=forms.CharField(label="duration", widget=forms.TextInput(attrs={
      'placeholder': 'Duration'
      }))
	intensity=forms.IntegerField(label="intensity", widget=forms.TextInput(attrs={
      'placeholder': 'Intensity'
      }))
	relsymp=forms.CharField(label="relsymp", widget=forms.TextInput(attrs={
      'placeholder': 'Related Symptoms'
      }))
	history=forms.CharField(label="history", widget=forms.TextInput(attrs={
      'placeholder': 'Past History'
      }))
	treat=forms.CharField(label="treat", widget=forms.TextInput(attrs={
      'placeholder': 'Treatment Taken At that Time'
      }))
	diag=forms.CharField(label="diag", widget=forms.TextInput(attrs={
      'placeholder': 'Diagnosis if any'
      }))
	premed=forms.CharField(label="premed", widget=forms.TextInput(attrs={
      'placeholder': 'Previous Medications'
      }))	
	diab=forms.CharField(label="diab", widget=forms.TextInput(attrs={
      'placeholder': 'Diabetic ?'
      }))	
	bp=forms.CharField(label="bp", widget=forms.TextInput(attrs={
      'placeholder': 'BP'
      }))	
	smokhab=forms.CharField(label="smokhab", widget=forms.TextInput(attrs={
      'placeholder': 'Smoking Habits'
      }))	
	weight=forms.CharField(label="weight", widget=forms.TextInput(attrs={
      'placeholder': 'Weight'
      }))
	height=forms.CharField(label="height", widget=forms.TextInput(attrs={
      'placeholder': 'Height'
      }))
'''class ChildrenForm(forms.Form):
	stomach=forms.CharField(label="stomach",required=False, widget=forms.TextInput(attrs={
      'placeholder': 'Stomachache'
      }))
	head=forms.CharField(label="head", required=False,widget=forms.TextInput(attrs={
      'placeholder': 'Headache'
      }))
	fever=forms.CharField(label="fever",required=False, widget=forms.TextInput(attrs={
      'placeholder': 'Fever'
      }))	
	flu=forms.CharField(label="flu",required=False, widget=forms.TextInput(attrs={
      'placeholder': 'Flu'
      }))
	sad=forms.CharField(label="sad",required=False, widget=forms.TextInput(attrs={
      'placeholder': 'Sad'
      }))
	itching=forms.CharField(label="itching", required=False,widget=forms.TextInput(attrs={
      'placeholder': 'Itching'
      }))
'''		
class DoctorResponseForm(forms.Form):
	advice=forms.CharField(label="advice", required=False,widget=forms.TextInput(attrs={
      'placeholder': 'Advice'
      }))	
	prec=forms.CharField(label="prec", required=False,widget=forms.TextInput(attrs={
      'placeholder': 'Itching'
      }))			
	pres=forms.CharField(label="pres", required=False,widget=forms.TextInput(attrs={
      'placeholder': 'Prescription'
      }))	
	
'''
class SelectpatForm(forms.Form):
	HOICES = (
      ("c", "C"),
      ("cpp", "C++"),
      ("java", "Java"),
      ("py", "Python"),
      ("rb", "Ruby"),
      )
    
	pat=forms.CharField(widget=forms.TextInput(attrs={
      'placeholder': 'Height'
      }))'''
