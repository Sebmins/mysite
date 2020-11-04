from django import forms
from django.forms import ModelForm
from django.utils.safestring import mark_safe

from quiz.models import QuizQuestions


class QuizForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title of quiz!"}))
    q1_answer = forms.CharField(
        initial="A = .., B = .., C = .., D = ..",
        widget=forms.Textarea(
            attrs={
                'rows': '2',
                'cols': '50',
            }
        ))

    q2_answer = forms.CharField(
        initial="A = .., B = .., C = .., D = ..",
        widget=forms.Textarea(
            attrs={
                'rows': '2',
                'cols': '50',
            }
        ))

    q3_answer = forms.CharField(
        initial="A = .., B = .., C = .., D = ..",
        widget=forms.Textarea(
            attrs={
                'rows': '2',
                'cols': '50',
            }
        ))

    q4_answer = forms.CharField(
        initial="A = .., B = .., C = .., D = ..",
        widget=forms.Textarea(
            attrs={
                'rows': '2',
                'cols': '50',
            }
        ))

    q5_answer = forms.CharField(
        initial="A = .., B = .., C = .., D = ..",
        widget=forms.Textarea(
            attrs={
                'rows': '2',
                'cols': '50',
            }
        ))

    class Meta:
        model = QuizQuestions
        fields = '__all__'

AtoB = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
]


class VotingForm(forms.Form):
    # name = forms.CharField()
    q1_selected = forms.ChoiceField(widget=forms.RadioSelect, choices=AtoB)
    q2_selected = forms.ChoiceField(widget=forms.RadioSelect, choices=AtoB)
    q3_selected = forms.ChoiceField(widget=forms.RadioSelect, choices=AtoB)
    q4_selected = forms.ChoiceField(widget=forms.RadioSelect, choices=AtoB)
    q5_selected = forms.ChoiceField(widget=forms.RadioSelect, choices=AtoB)

    def __init__(self, *args, **kwargs):
        quiz = kwargs.pop("quiz")
        super(VotingForm, self).__init__(*args, **kwargs)

        # self.fields[str('name')].label = quiz.name
        self.fields[str('q1_selected')].label = mark_safe(quiz.q1_question + " <br/><br/> " + quiz.q1_answer)
        self.fields[str('q2_selected')].label = mark_safe(quiz.q2_question + " <br/><br/> " + quiz.q2_answer)
        self.fields[str('q3_selected')].label = mark_safe(quiz.q3_question + " <br/><br/> " + quiz.q3_answer)
        self.fields[str('q4_selected')].label = mark_safe(quiz.q4_question + " <br/><br/> " + quiz.q4_answer)
        self.fields[str('q5_selected')].label = mark_safe(quiz.q5_question + " <br/><br/> " + quiz.q5_answer)



