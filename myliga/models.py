from django.db import models
from django.db.models.fields import CharField


class Manager(models.Model):
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, null=True)
    contact_no = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class User(models.Model):
    manager = models.ForeignKey(Manager)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username