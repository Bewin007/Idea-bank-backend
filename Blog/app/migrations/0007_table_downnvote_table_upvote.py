# Generated by Django 4.0.8 on 2023-02-21 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_email_user_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='downnvote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='table',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
    ]
