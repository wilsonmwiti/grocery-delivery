# Generated by Django 3.0.3 on 2020-02-13 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Categories'),
        ),
    ]
