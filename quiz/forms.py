from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit, ButtonHolder
from django import forms
from django.forms import ModelForm, inlineformset_factory
from quiz.models import Quiz, QuizQuestion


class QuestionForm(ModelForm):
    class Meta:
        model = QuizQuestion
        exclude = ('quiz',)


EditFormSet = inlineformset_factory(Quiz, QuizQuestion, form=QuestionForm, extra=1)
CreateFormSet = inlineformset_factory(Quiz, QuizQuestion, form=QuestionForm, extra=1)


class VotingForm(forms.Form):
    def __init__(self, *args, **kwargs):
        quiz = kwargs.pop('quiz')
        super(VotingForm, self).__init__(*args, **kwargs)

        i = 0
        for question in quiz:
            self.helper = FormHelper()
            self.helper.form_id = 'form_question'
            self.helper.form_class = 'blueForms'
            self.helper.add_input(Submit('submit','Submit',
                                         css_id="submitBtn",
                                         css_class='btn btn-primary btn-lg btn-block'))
            self.fields['question_text' + str(i)] = forms.ChoiceField(
                widget=forms.RadioSelect, label=question, choices=[
                    (1, quiz[i].option1),
                    (2, quiz[i].option2),
                    (3, quiz[i].option3),
                    (4, quiz[i].option4), ])
            i = i + 1
