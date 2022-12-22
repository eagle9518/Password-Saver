"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path

from accounts import views as account_views
from password_manager import views as password_views

urlpatterns = [
    path('', password_views.home_page, name='home'),
    path('new_category', password_views.new_category, name='new_category'),
    path('category/<int:pk>', password_views.category_pages, name='category'),
    path('category/<int:pk>/new_password', password_views.new_password, name='new_password'),

    path('signup', account_views.signup, name='signup'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('admin/', admin.site.urls),
]
