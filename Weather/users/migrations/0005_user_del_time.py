# Generated by Django 4.2.16 on 2024-11-04 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_city_name_user_users_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='del_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Deletion Time'),
        ),
    ]
