# Generated by Django 4.2.6 on 2023-12-17 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_billing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billing',
            name='cus_name',
        ),
    ]
