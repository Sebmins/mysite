from django import forms
from django.forms import ModelForm, inlineformset_factory
from django.utils import timezone
from quiz.models import Quiz, QuizQuestion


class EditForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title of quiz!"}))
    author = forms.CharField()
    dt_date = forms.DateTimeField(initial=timezone.now())

    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionForm(ModelForm):
    class Meta:
        model = QuizQuestion
        exclude = ('quiz',)


EditFormSet = inlineformset_factory(Quiz, QuizQuestion, form=QuestionForm, extra=0)
CreateFormSet = inlineformset_factory(Quiz, QuizQuestion, form=QuestionForm, extra=5)

AtoB = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
]


class VotingForm(forms.Form):
    title = forms.CharField()
    author = forms.CharField()
    dt_date = forms.DateField()
    question_text = forms.CharField()

    def __init__(self, *args, **kwargs):
        quiz = kwargs.pop("quiz")
        # question = kwargs.pop("question")
        super(VotingForm, self).__init__(*args, **kwargs)

        self.fields[str('title')].label = quiz.title
        self.fields[str('author')].label = "Written by: " + quiz.author
        self.fields[str('dt_date')].lable = "hi"
        # self.fields[str('question_text')].label = question.question_text


class VotingForm2(forms.Form):
    question_text = forms.CharField()
    option1 = forms.CharField()
    option2 = forms.CharField()
    option3 = forms.CharField()
    option4 = forms.CharField()

    def __init__(self, *args, **kwargs):
        quiz = kwargs.pop("quiz")
        super(VotingForm, self).__init__(*args, **kwargs)

        self.fields[str('question_text')].label = quiz.question_text
        self.fields[str('option1')].label = "A: " + quiz.option1
        self.fields[str('option2')].label = "B: " + quiz.option2
        self.fields[str('option3')].label = "C: " + quiz.option3
        self.fields[str('option4')].label = "D: " + quiz.option4

