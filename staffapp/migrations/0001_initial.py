# Generated by Django 3.0.3 on 2020-02-13 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_sold', models.DateTimeField(auto_now_add=True)),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staffapp.Payments')),
            ],
            options={
                'verbose_name_plural': 'sales',
                'db_table': 'sales',
            },
        ),
    ]
