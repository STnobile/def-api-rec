# Generated by Django 3.2.21 on 2023-09-17 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='../dfl_profile_xaqecn.png', upload_to='images/'),
        ),
    ]
