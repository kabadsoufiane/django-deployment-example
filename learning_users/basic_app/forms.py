from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfoFrom

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoFrom(forms.ModelForm):
    class Meta():
        model = UserProfileInfoFrom
        fields = ('portfolio_site', 'profile_pic')