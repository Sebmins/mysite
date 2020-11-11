from django.db import models
from django.utils import timezone

One_to_Four = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
]


class Quiz(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    dt_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title

    def quizquestion(self):
        return self.quizquestion_set.all()

    class Meta:
        verbose_name = 'Quizze'


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=100)
    correct = models.IntegerField(blank=True, null=True, choices=One_to_Four)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)

    def __str__(self):
        return self.question_text
