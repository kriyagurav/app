# Generated by Django 4.0.3 on 2022-03-12 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_employeedetails_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeedetails',
            old_name='User',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='employeedetails',
            name='password',
        ),
    ]