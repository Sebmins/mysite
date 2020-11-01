from django import forms
from django.forms import ModelForm
from quiz.models import QuizQuestions


class QuizForm(ModelForm):
    class Meta:
        model = QuizQuestions
        fields = '__all__'
        labels = {
            'q1_answer': 'Answer to the question',
        }
        help_texts = {
            'q1_answer': 'Should look like, "A = AnswerA, B = AnswerB,..."',
        }
        error_messages = {
            'name': {
                'max_length': "Title of the quiz shouldn't be greater than 20 characters",
            },
        }


class RawQuizForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title of quiz!"}))

    q1_question = forms.CharField()
    q1_answer = forms.CharField(
        initial="A = England, B = France, C = Spain, D = Germany",
        widget=forms.Textarea(
            attrs={
                "rows": 2,
                "col": 400,
            }
        ))
    q1_correct = forms.CharField()
    q1_selected = forms.CharField()