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


class VotingFormPrimary(forms.Form):
    title = forms.CharField()
    author = forms.CharField()
    dt_date = forms.DateField()
    question_text = forms.CharField()

    def __init__(self, *args, **kwargs):
        quiz = kwargs.pop("quiz")
        # question = kwargs.pop("question")
        super(VotingFormPrimary, self).__init__(*args, **kwargs)

        self.fields[str('title')].label = quiz.title
        self.fields[str('author')].label = "Written by: " + quiz.author
        self.fields[str('dt_date')].lable = "hi"
        # self.fields[str('question_text')].label = question.question_text


class VotingForm(forms.Form):
    question_text = forms.ChoiceField(widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        quiz = kwargs.pop("quiz")
        super(VotingForm, self).__init__(*args, **kwargs)
        One_to_four = [
            (1, quiz.option1),
            (2, quiz.option2),
            (3, quiz.option3),
            (4, quiz.option4),
        ]
        self.fields[str('question_text')].label = quiz.question_text
        self.fields[str('question_text')].choices = One_to_four
