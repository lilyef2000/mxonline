# _*_ coding:utf-8 _*_
__author__ = 'antenna'
__date__ = '18-1-2 下午4:00'
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)