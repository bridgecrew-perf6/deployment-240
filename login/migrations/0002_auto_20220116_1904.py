# Generated by Django 2.2.9 on 2022-01-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='login_details',
            name='isactive',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterModelTable(
            name='login_details',
            table='LOGIN_MASTER',
        ),
    ]
