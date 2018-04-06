from django import forms
from .models import User,UserInfo
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    class Meta():
        model = User
        fields = ('username', 'email' , 'password1','password2')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
        


class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('gender','profile_pic')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['gender'].label = 'Gender'
        self.fields['profile_pic'].label = 'Profile Picture'
