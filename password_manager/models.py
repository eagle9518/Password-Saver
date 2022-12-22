from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class Category(models.Model):
    name = models.CharField(max_length=256, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category', null=True)

    def __str__(self):
        return self.name


class Site(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='site', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='site')
    site = models.CharField(max_length=256)
    username = models.CharField(max_length=256, unique=True)
    password = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.site
