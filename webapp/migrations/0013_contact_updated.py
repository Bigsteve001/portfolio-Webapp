# Generated by Django 4.1 on 2022-08-08 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_contact_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
