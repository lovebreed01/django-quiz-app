# Generated by Django 3.2.2 on 2021-07-23 09:54

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizapp', '0002_alter_question_taker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='taker',
            field=models.ForeignKey(default=django.contrib.auth.models.AnonymousUser, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
