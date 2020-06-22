from django import forms
from .models import *


class SignupForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'pw', 'email', 'birth', 'gender']


class SigninForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'pw']


class PostForm(forms.ModelForm):
    class Meta:
        model = PostMountain
        fields = ['imgpath', 'name', 'body', 'star']

