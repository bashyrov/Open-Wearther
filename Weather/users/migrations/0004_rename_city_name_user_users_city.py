# Generated by Django 4.2.16 on 2024-11-01 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_tg_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='city_name',
            new_name='users_city',
        ),
    ]
