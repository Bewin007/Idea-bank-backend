# Generated by Django 4.0.8 on 2023-02-21 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_table_downnvote_table_upvote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='downnvote',
            new_name='downvote',
        ),
    ]
