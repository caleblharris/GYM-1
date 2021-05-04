from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from .models import Customer

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from .forms import (
    CustomerModelForm,
    CustomUserCreationForm,
    CustomAuthenticationForm,
    
)


class Hero(generic.ListView):
    model = Customer
    context_object_name = 'customer'
    template_name = 'hero.html'
    authentication_form = CustomAuthenticationForm
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('index')


class Index(generic.ListView):
    model = Customer
    context_object_name = 'customer'
    template_name = 'index.html'
    

    




class CustomerCreateView(BSModalCreateView):
    template_name = 'create_customer.html'
    form_class = CustomerModelForm
    success_message = 'Success: Customer was created.'
    success_url = reverse_lazy('index')


class CustomerUpdateView(BSModalUpdateView):
    model = Customer
    template_name = 'update_customer.html'
    form_class = CustomerModelForm
    success_message = 'Success: Customer was updated.'
    success_url = reverse_lazy('index')


class CustomerReadView(BSModalReadView):
    model = Customer
    template_name = 'read_customer.html'


class CustomerDeleteView(BSModalDeleteView):
    model = Customer
    template_name = 'delete_customer.html'
    success_message = 'Success: Customer was deleted.'
    success_url = reverse_lazy('index')


class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('index')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('index')



# Create your views here.
from .models import *

class CustomerCreateView(BSModalCreateView):
    template_name = 'create_customer.html'
    form_class = CustomerModelForm
    success_message = 'Success: Customer was created.'
    success_url = reverse_lazy('index')

def Customer(request):
    data = dict()
    if request.method == 'GET':
        customer = Customer.objects.all()
        # asyncSettings.dataKey = 'table'
        data['table'] = render_to_string(
            '_customer_table.html',
            {'customer': customer},
            request=request
        )
        return JsonResponse(data)    
