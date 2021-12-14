from django.contrib.auth.models import (
    AbstractUser, BaseUserManager, AbstractBaseUser)
from django.db import models
from django.utils import timezone

from oscar.core import compat
from oscar.apps.customer import abstract_models

# A simple extension of the core Oscar User model
class User(abstract_models.AbstractUser):
    # twitter_username = models.CharField(max_length=255, unique=True)
    user_discount = models.IntegerField(help_text='User discount', null=True, default=0)
    user_phone = models.CharField(help_text='User phone', max_length=20, null=True, default='')
