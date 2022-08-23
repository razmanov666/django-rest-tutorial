# Generated by Django 4.1 on 2022-08-23 14:39
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("women", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="women",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
            preserve_default=False,
        ),
    ]
