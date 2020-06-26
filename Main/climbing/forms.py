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


