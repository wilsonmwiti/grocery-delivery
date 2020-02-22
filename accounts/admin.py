# Register your models here.
from django.contrib import admin

# the module name is app_name.models
from accounts.models import User


# username = models.CharField(max_length=20)
#     email = models.EmailField(max_length=255, unique=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     user_status = models.CharField(max_length=20, null=False, default="active")
#     timestamp = models.DateTimeField(auto_now_add=True)
#     phone_number = models.CharField(unique=True, null=True, blank=True, max_length=20)
#     user_type = models.CharField(default="customer", max_length=20)
#     email_confirmed = models.BooleanField(default=False)
#     location = models.CharField(max_length=30)

class UserAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'username', 'email', 'is_admin', 'is_staff', 'user_status', 'phone_number', 'location', 'user_type',
    'email_confirmed',)
    search_fields = ('username', 'email', 'user_type', 'phone_number',)


# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(User, UserAdmin)
