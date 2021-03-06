# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Payment
from app.models import Comment
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['subject','detail','rate']
# class PaymentForm(forms.Form):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder" : "Username",                
#                 "class": "form-control"
#             }
#         ))
#     # address = forms.EmailField(
#     #     widget=forms.TextInput(
#     #         attrs={
#     #             "id" : "input-address",                
#     #             "class": "form-control"
#     #         }
#     #     ))
#     # first_name = forms.CharField(
#     #     widget=forms.TextInput(
#     #         attrs={
#     #             "placeholder" : "Password",                
#     #             "class": "form-control"
#     #         }
#     #     ))
#     # phone_number = forms.CharField(
#     #     widget=forms.TextInput(
#     #         attrs={
#     #             "id" : "input-phonenumber",                
#     #             "class": "form-control"
#     #         }
#     #     ))
#     # city = forms.ChoiceField(
#     #     widget=forms.ChoiceField(
#     #         attrs={
#     #             "id" : "input-province",                
#     #             "class": "form-control"
#     #         }
#     #     ))
#     # district = forms.ChoiceField(
#     #     widget=forms.ChoiceField(
#     #         attrs={
#     #             "id" : "input-district",                
#     #             "class": "form-control"
#     #         }
#     #     ))
#     # ward = forms.ChoiceField(
#     #     widget=forms.ChoiceField(
#     #         attrs={
#     #             "id" : "input-district",                
#     #             "class": "form-control"
#     #         }
#     #     ))
#     # class Meta:
#     #     model = User
#     #     fields = ('username', 'firstname', 'phonenumber', 'password2')
