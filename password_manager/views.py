import json

from django.contrib.auth.models import User
from django.db.models import Exists, OuterRef
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from password_manager.forms import NewCategoryForm, NewPasswordForm
# Create your views here.
from password_manager.models import Category, Site


def home_page(request):
    if request.method == "POST":
        category_to_delete = json.loads(request.body).get("category_to_delete")
        request.user.category.get(name=category_to_delete).delete()

        data = {"Delete Message": "{} Deleted".format(category_to_delete)}
        return JsonResponse(data)

    return render(request, 'home.html')


def new_category(request):
    if request.method == 'POST':
        form = NewCategoryForm(request.POST)
        if form.is_valid():
            request.user.category.create(
                name=form.cleaned_data.get('category')
            )
            return redirect("home")
    else:
        form = NewCategoryForm()
    return render(request, 'new_category.html', {'form': form})


def category_pages(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        password_to_delete = json.loads(request.body).get("password_to_delete")
        request.user.site.get(site=password_to_delete).delete()

        data = {"Delete Message": "{} Deleted".format(password_to_delete)}
        return JsonResponse(data)

    return render(request, 'category.html', {'category': category})


def new_password(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = NewPasswordForm(request.POST)
        if form.is_valid():
            request.user.site.create(
                category=category,
                site=form.cleaned_data.get('site'),
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            return redirect("category", pk=pk)
    else:
        form = NewPasswordForm()

    return render(request, 'new_password.html', {'category': category, 'form': form})
