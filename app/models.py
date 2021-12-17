from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    push_token = models.CharField(max_length=150)
    username = models.CharField(blank=True, null=True, max_length=150)
    projects = models.ManyToManyField("Project", related_name='users')

    def __str__(self):
        return self.email


class Project(models.Model):
    json = models.JSONField()
    datecreate = models.DateField(auto_now_add=True)
    dateupdate = models.DateField(auto_now=True)
    projectname = models.TextField()

    def __str__(self):
        return self.projectname
