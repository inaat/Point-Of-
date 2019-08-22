from django import forms
from django.db import connections ,connection
import socket
from django.shortcuts import redirect






class Login_Form(forms.Form):
    User_Id = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input100',
        'placeholder': 'User Id',
         'type':'text'
       
    }))
    Location_Id = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input100',
        'placeholder': 'Location Id',
        'type':'text'
    }))
    Password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input100',
        'placeholder': 'Password',
        'type':'password'
    }))

    def clean(self):
        cleaned_data = super().clean()
        User_Id = cleaned_data.get('User_Id')
        Location_Id = cleaned_data.get('Location_Id')
        Password = cleaned_data.get('Password')
        cursor = connections["form2_db"].cursor()
        cursor.execute("CALL `genprocandfunctions`.`User_Login`(@ReturnMessage, @TradeCode, @ProjectCode, @BranchCode,@UserName,@userType, '{}', '{}' , '{}' , '{}' )".format(socket.gethostname(),User_Id , Location_Id, Password))
        cursor.execute("SELECT @ReturnMessage;")
        vl = cursor.fetchone()
        
       
        tup = ''
        for vl in vl:
            tup = vl
      
        
        if User_Id and Password:

            if  tup == 'Login Succssed':
                pass

            elif tup == tup :
                raise forms.ValidationError(tup)






            



        