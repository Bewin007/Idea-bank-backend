# Generated by Django 4.0.8 on 2023-03-06 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0013_votelog_delete_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votelog',
            name='voted_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes_received', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='votelog',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes_cast', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
