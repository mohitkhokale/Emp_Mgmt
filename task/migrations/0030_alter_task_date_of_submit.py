# Generated by Django 4.0.3 on 2022-03-10 11:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0029_remove_assigntask_task_assigntask_task_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_of_submit',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 10, 17, 28, 13, 789663)),
        ),
    ]