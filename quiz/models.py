from django.db import models
from django.forms import ModelForm
from django.http import request
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

TITLE_CHOICES = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
]


class QuizQuestions(models.Model):
    name = models.CharField(max_length=20)

    q1_question = models.CharField(max_length=200)
    q1_answer = models.CharField(blank=True, max_length=200)
    q1_correct = models.CharField(blank=True, max_length=1, choices=TITLE_CHOICES)
    q1_selected = models.CharField(blank=True, editable=False, max_length=1)

    q2_question = models.CharField(max_length=200)
    q2_answer = models.CharField(blank=True, max_length=200)
    q2_correct = models.CharField(blank=True, max_length=1, choices=TITLE_CHOICES)
    q2_selected = models.CharField(blank=True, editable=False, max_length=1)

    q3_question = models.CharField(max_length=200)
    q3_answer = models.CharField(blank=True, max_length=200)
    q3_correct = models.CharField(blank=True, max_length=1, choices=TITLE_CHOICES)
    q3_selected = models.CharField(blank=True, editable=False, max_length=1)

    q4_question = models.CharField(max_length=200)
    q4_answer = models.CharField(blank=True, max_length=200)
    q4_correct = models.CharField(blank=True, max_length=1, choices=TITLE_CHOICES)
    q4_selected = models.CharField(blank=True, editable=False, max_length=1)

    q5_question = models.CharField(max_length=200)
    q5_answer = models.CharField(blank=True, max_length=200)
    q5_correct = models.CharField(blank=True, max_length=1, choices=TITLE_CHOICES)
    q5_selected = models.CharField(blank=True, editable=False, max_length=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Quiz Question'

    def get_absolute_url(self):
        question = get_object_or_404(QuizQuestions, pk=id)
        return render(request, 'quiz/questionnaire.html', {'question': question})


class Answer(models.Model):
    question = models.ForeignKey(QuizQuestions, on_delete=models.CASCADE)


