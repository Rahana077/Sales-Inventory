# Generated by Django 4.2.6 on 2023-12-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_delete_notification_count_remove_notification_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]