# Generated by Django 4.2.6 on 2023-12-07 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.sale')),
            ],
        ),
    ]