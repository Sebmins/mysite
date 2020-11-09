import datetime
from pyexpat import model

from django.db.models import Model, DateTimeField, CharField, ForeignKey, CASCADE, IntegerField
from django.utils import timezone


class PollQuestion(Model):
    question_text = CharField(max_length=200)
    pub_date = DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    class Meta:
        verbose_name = 'Poll Question'


class Choice(Model):
    question = ForeignKey(PollQuestion, on_delete=CASCADE)
    choice_text = CharField(max_length=200)
    votes = IntegerField(default=0)

    def __str__(self):
        return self.choice_text
