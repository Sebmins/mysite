from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, FormView, UpdateView

from .forms import QuizForm
from .models import QuizQuestions


class IndexView(ListView):
    template_name = "quiz/index.html"
    queryset = QuizQuestions.objects.all()
    # queryset = QuizQuestions.objects.order_by('-id').all()


class QuizView(DetailView):
    template_name = 'quiz/questionnaire.html'

    def get_object(self):
        question_id = self.kwargs.get("question_id")
        return get_object_or_404(QuizQuestions, id=question_id)


class VoteView(FormView):
    template_name = "quiz/results.html"
    form_class = QuizForm

    def get_object(self):
        question_id = self.kwargs.get("question_id")
        return get_object_or_404(QuizQuestions, id=question_id)


class ResultsView(ListView):
    # model = Answer
    template_name = 'quiz/results.html'


class AddView(CreateView):
    template_name = 'quiz/create.html'
    form_class = QuizForm
    queryset = QuizQuestions.objects.all()
    success_url = '../'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class DeleteView(DeleteView):
    model = QuizQuestions
    template_name = 'quiz/delete.html'
    success_url = '../../'


class EditView(UpdateView):
    model = QuizQuestions
    template_name = 'quiz/create.html'
    form_class = QuizForm

    def get_object(self):
        quiz_id = self.kwargs.get("question_id")
        return get_object_or_404(QuizQuestions, id=quiz_id)


# FORM VIEW?
def vote(request, question_id):
    quiz = get_object_or_404(QuizQuestions, pk=question_id)
    try:
        selected_choice = request.POST['group1']
        selected_choice2 = request.POST['group2']
        selected_choice3 = request.POST['group3']
        selected_choice4 = request.POST['group4']
        selected_choice5 = request.POST['group5']
    except(KeyError, QuizQuestions.DoesNotExist):
        return render(request, 'quiz/votingError.html')
    else:
        quiz.q1_selected = selected_choice
        quiz.q2_selected = selected_choice2
        quiz.q3_selected = selected_choice3
        quiz.q4_selected = selected_choice4
        quiz.q5_selected = selected_choice5
        quiz.save()

        context = {
            "quiz": quiz
        }

        return render(request, 'quiz/results.html', context)

