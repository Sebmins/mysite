from django import forms
from django.forms import ModelForm
from quiz.models import Quiz, QuizQuestion

class VotingForm(forms.Form):

    title = forms.CharField()
    author = forms.CharField()
    # question_text = forms.CharField()
    # q2_selected = forms.ChoiceField(widget=forms.RadioSelect, choices=AtoB)
    # q3_selected = forms.ChoiceField(widget=forms.RadioSelect, choices=AtoB)
    # q4_selected = forms.ChoiceField(widget=forms.RadioSelect, choices=AtoB)
    # q5_selected = forms.ChoiceField(widget=forms.RadioSelect, choices=AtoB)


    def __init__(self, *args, **kwargs):
        quiz = kwargs.pop("quiz")
        super(VotingForm, self).__init__(*args, **kwargs)

        self.fields[str('title')].label = quiz.title
        self.fields[str('author')].label = "Written by: " + quiz.author
        # self.fields[str('question_text')].label = mark_safe(quiz.question_text + " <br/><br/> " + quiz.q2_answer)
    #     self.fields[str('q3_selected')].label = mark_safe(quiz.q3_question + " <br/><br/> " + quiz.q3_answer)
    #     self.fields[str('q4_selected')].label = mark_safe(quiz.q4_question + " <br/><br/> " + quiz.q4_answer)
    #     self.fields[str('q5_selected')].label = mark_safe(quiz.q5_question + " <br/><br/> " + quiz.q5_answer)


class NewQuizForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title of quiz!"}))
    author = forms.CharField()
    question_text = forms.CharField()

    class Meta:
        model = Quiz
        fields = '__all__'


AtoB = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
]



