# Generated by Django 4.1 on 2022-08-08 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_rename_service_1_description_services_service_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='service_description',
            new_name='service_1_description',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='service_name',
            new_name='service_1_name',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='service_price',
            new_name='service_1_price',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='updated',
        ),
        migrations.AddField(
            model_name='services',
            name='service_2_description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='service_2_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='service_2_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='service_3_description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='service_3_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='service_3_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='service_4_description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='service_4_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='service_4_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
