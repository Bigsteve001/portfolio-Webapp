# Generated by Django 4.1 on 2022-09-29 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_alter_form_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='message',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]