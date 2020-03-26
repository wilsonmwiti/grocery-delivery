# Generated by Django 3.0.3 on 2020-03-26 21:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('staffapp', '0003_contactmessages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('time_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Subscribers',
                'db_table': 'Subscribers',
            },
        ),
    ]
