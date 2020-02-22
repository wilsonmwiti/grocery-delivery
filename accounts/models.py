from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=True, is_company=True,
                    is_superuser=False, user_type='customer'):
        if not email:
            raise ValueError("user requires an email")
        if not password:
            raise ValueError("user requires a password")
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.is_company = is_company
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_active = is_active
        user_obj.is_admin = is_admin
        user_obj.is_superuser = is_superuser
        user_obj.user_type = user_type
        user_obj.save(using=self._db)
        return user_obj

    #     create customer-accounts for access to statistical panel
    def create_staffuser(self, email, password=None, is_staff=True, is_admin=False, is_active=True):
        user = self.create_user(email, password=password, is_staff=is_staff, is_admin=is_admin, is_active=is_active,
                                is_company=False, is_superuser=False, user_type='staff'
                                )
        return user

    #     create admin account for site admins
    def create_superuser(self, email, password=None, is_staff=True, is_admin=True, is_active=True):
        user = self.create_user(email, password=password, is_staff=is_staff, is_admin=is_admin, is_active=is_active,
                                is_company=False, is_superuser=True, user_type='admin'
                                )
        return user


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    user_status = models.CharField(max_length=20, null=False, default="active")
    timestamp = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(unique=True, null=True, blank=True, max_length=20)
    user_type = models.CharField(default="customer", max_length=20)
    email_confirmed = models.BooleanField(default=False)
    location = models.CharField(max_length=30)
    USERNAME_FIELD = 'email'  # make email username field
    objects = UserManager()

    class Meta:
        db_table = "Users"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email

    @property
    def user_is_admin(self):
        return self.is_admin

    @property
    def user_is_staff(self):
        return self.is_staff

    @property
    def user_is_active(self):
        return self.is_active
