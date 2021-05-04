"""djangotest1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views




urlpatterns = [
    
    path('', views.Hero.as_view(), name='home'),
    path('index/', views.Index.as_view(), name='index'),
    path('create/', views.CustomerCreateView.as_view(), name='create_customer'),
    path('update/<int:pk>', views.CustomerUpdateView.as_view(), name='update_customer'),
    path('read/<int:pk>', views.CustomerReadView.as_view(), name='read_customer'),
    path('delete/<int:pk>', views.CustomerDeleteView.as_view(), name='delete_customer'),
    #path('customer/', views.customer, name='customer'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLoginView.as_view(), name='logout'),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
]