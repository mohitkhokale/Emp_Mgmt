# Generated by Django 4.0.3 on 2022-03-10 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0038_alter_task_date_of_submit_delete_assigntask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_of_submit',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 10, 20, 49, 44, 786485)),
        ),
    ]
