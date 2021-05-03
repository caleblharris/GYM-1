from .models import Customer
from bootstrap_modal_forms.forms import BSModalModelForm

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class CustomerModelForm(BSModalModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'gender', 'email','phone_number','address_name','instructor_name']

class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']