# Generated by Django 4.0.3 on 2022-03-10 10:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0024_alter_task_date_of_submit_alter_task_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_of_submit',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 10, 15, 47, 35, 179499)),
        ),
        migrations.AlterField(
            model_name='task',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emp', to=settings.AUTH_USER_MODEL),
        ),
    ]
