# Generated by Django 3.1.2 on 2020-10-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20201029_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizquestions',
            name='q1_correct',
            field=models.IntegerField(default=0),
        ),
    ]
