# Generated by Django 3.1.2 on 2020-10-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_auto_20201029_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizquestions',
            name='q1_answer',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='quizquestions',
            name='q1_question',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quizquestions',
            name='q2_answer',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='quizquestions',
            name='q2_question',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quizquestions',
            name='q3_answer',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='quizquestions',
            name='q3_question',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quizquestions',
            name='q4_answer',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='quizquestions',
            name='q4_question',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quizquestions',
            name='q5_answer',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='quizquestions',
            name='q5_question',
            field=models.CharField(max_length=200),
        ),
    ]
