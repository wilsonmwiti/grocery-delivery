from enum import Enum

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
# Create your models here.
from django.utils.safestring import mark_safe

from accounts.models import User


class StoreLine(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    logo = models.ImageField(upload_to='images/stores/')
    time_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "lines"
        verbose_name_plural = "lines"

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % self.logo.url)

    image_tag.short_description = 'Logo'
    image_tag.allow_tags = True


class Stores(models.Model):
    line = models.ForeignKey(StoreLine, on_delete=models.CASCADE)
    town = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    time_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=12)

    class Meta:
        db_table = 'stores'
        verbose_name_plural = 'stores'


class OpeningHours(models.Model):
    class Days(Enum):
        Monday = ('Monday', "Monday")
        Tuesday = ('Tuesday', "Tuesday")
        Wednesday = ('Wednesday', "Wednesday")
        Thursday = ('Thursday', "Thursday")
        five = ('Friday', "Friday")
        Friday = ('Saturday', "Saturday")
        Sunday = ('Sunday', "Sunday")

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    store = models.ForeignKey(
        Stores, on_delete=models.CASCADE
    )
    weekday = models.CharField(max_length=9,
                               choices=[x.value for x in Days],
                               default=Days.get_value('Monday')
                               )
    from_hour = models.TimeField()
    to_hour = models.TimeField()