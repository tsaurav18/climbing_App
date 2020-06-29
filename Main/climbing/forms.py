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
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': '사용자 이름'}
            ),
            'password': forms.PasswordInput(
                attrs={'placeholder': '비밀번호'}
            )
        }


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
            'body': forms.Textarea(
                attrs={'class': 'content', 'placeholder': 'Type here'}
            ),
            'star':forms.NumberInput(
                  attrs={'class': 'star', 'placeholder': '0'}
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


class Record2Form(forms.ModelForm):
    class Meta:
        model = MyList
        fields = ['m_name', 'course']
        widgets = {
            'm_name' : forms.TextInput(
                attrs={'class':'form-input1', 'placeholder': '산 이름'}
            ),
            'course': forms.TextInput(
                attrs={'class': 'form-input1', 'placeholder': '코스 이름'}
            )
        }

