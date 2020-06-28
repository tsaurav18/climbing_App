from django import forms
from .models import *


class SignupForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'password', 'email', 'birth', 'gender']


class SigninForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'password']


class PostForm(forms.ModelForm):
    class Meta:
        model = PostMountain
        fields = ['img', 'name', 'body', 'star']
        widgets = {
            'img': forms.FileInput(
                attrs={'class': 'row_box', 'placeholder': 'Title'}
            ),
            'name': forms.TextInput(
                attrs={'class': 'row_info', 'placeholder': 'Name'}
            ),
            'body': forms.TextInput(
                attrs={'class': 'content', 'placeholder': 'Type here'}
            )
        }


class RecordForm(forms.ModelForm):
    class Meta:
        model = MyList
        fields = ['m_name', 'course', 'time']
        widgets = {
            'm_name' : forms.TextInput(
                attrs={'class':'form-input1', 'placeholder': '산 이름'}
            ),
            'course': forms.TextInput(
                attrs={'class': 'form-input1', 'placeholder': '코스 이름'}
            ),
            'time': forms.TextInput(
                attrs={'class': 'form-input1', 'placeholder': '소요 시간'}
            ),
        }


