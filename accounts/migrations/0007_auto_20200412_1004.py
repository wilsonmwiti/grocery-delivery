# Generated by Django 3.0.3 on 2020-04-12 10:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0006_user_hash'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='unknown', max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE,
                                              to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]