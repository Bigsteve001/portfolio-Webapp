# Generated by Django 4.1 on 2022-10-07 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0023_alter_form_message_alter_form_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
