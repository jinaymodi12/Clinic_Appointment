# Generated by Django 4.0.4 on 2022-05-12 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_alter_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
