# Generated by Django 3.2.21 on 2023-09-18 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='user',
            new_name='owner',
        ),
    ]
