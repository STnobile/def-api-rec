# Generated by Django 3.2.21 on 2023-09-20 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_booking_booking_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booking_count',
            new_name='booked_count',
        ),
    ]
