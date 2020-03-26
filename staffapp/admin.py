from django.contrib import admin

# Register your models here.
from staffapp.models import *


# class UserAdmin(admin.ModelAdmin):
#     list_display = (
#     'id', 'username', 'email', 'is_admin', 'is_staff', 'user_status', 'phone_number', 'location', 'user_type',
#     'email_confirmed',)
#     search_fields = ('username', 'email', 'user_type', 'phone_number',)
#
#
# # Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
# admin.site.register(User, UserAdmin)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['sender_mail', 'sender_name', 'mail_subject', 'mail_message', 'time_sent', 'is_read']
    search_fields = ['sender_mail', 'sender_name', 'mail_subject']
    readonly_fields = [x for x in list_display[0:5]]
    labels = {
        'is_read': 'Mark as read',
    }


admin.site.register(Payments)
admin.site.register(Sales)
admin.site.register(ContactMessages, ContactsAdmin)
