# Generated by Django 4.0.8 on 2023-02-16 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='Name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='Password',
            field=models.CharField(max_length=65),
        ),
        migrations.AlterField(
            model_name='user',
            name='UserID',
            field=models.CharField(max_length=255),
        ),
    ]
