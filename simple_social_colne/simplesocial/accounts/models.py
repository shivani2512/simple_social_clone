from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import PermissionsMixin


class User(User, PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

