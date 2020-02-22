# Generated by Django 3.0.3 on 2020-02-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0003_user_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(
                choices=[('admin', 'admin account'), ('customer', 'customer account'), ('satff', 'staff account')],
                default='customer', max_length=32),
        ),
    ]
