# Generated by Django 4.0.8 on 2023-03-05 06:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_table_downvote_remove_table_upvote_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='vote',
            name='is_upvote',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vote',
            name='voted_before',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vote',
            name='voted_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote',
        ),
    ]
