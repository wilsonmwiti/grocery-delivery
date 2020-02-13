# Generated by Django 3.0.3 on 2020-02-13 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('time_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('amount_remaining', models.CharField(max_length=20)),
                ('time_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'inventory items',
                'db_table': 'Inventory',
            },
        ),
    ]
