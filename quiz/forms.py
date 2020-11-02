from django import forms
from django.forms import ModelForm
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
