# Generated by Django 4.0.3 on 2022-03-10 04:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_alter_task_employee_alter_task_date_of_submit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_of_submit',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 10, 10, 4, 57, 404658)),
        ),
    ]