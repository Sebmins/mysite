
from django.db import models
from django.urls import reverse
from django.utils import timezone

TITLE_CHOICES = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
]


class Quiz(models.Model):
    title = models.CharField(default="qTitle", max_length=40)
    author = models.CharField(default="Seb", max_length=40)
    dt_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Quizze'


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(default="text", max_length=100)
    option1 = models.CharField(default="1", max_length=50)
    option2 = models.CharField(default="2", max_length=50)
    option3 = models.CharField(default="3", max_length=50)
    option4 = models.CharField(default="4", max_length=50)

    def __str__(self):
        return self.question_text
