# Generated by Django 4.1 on 2022-08-08 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_team_members_job_team_members_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
