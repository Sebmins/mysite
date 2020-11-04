from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, FormView, UpdateView

from .forms import VotingForm, NewQuizForm
from .models import Quiz, QuizQuestion


class IndexView(ListView):
    template_name = "quiz/index.html"
    queryset = Quiz.objects.all()
    # queryset = QuizQuestions.objects.order_by('-id').all()


class QuizView(FormView, DetailView):
    model = Quiz
    template_name = 'quiz/questionnaire.html'
    form_class = NewQuizForm

    def get_object(self):
        quiz_id = self.kwargs.get("quiz_id")
        return get_object_or_404(Quiz, id=quiz_id)

    def get_form_kwargs(self):
        kwargs = super(QuizView, self).get_form_kwargs()
        quiz_id = Quiz.objects.get(pk=self.kwargs["quiz_id"])
        kwargs['quiz'] = quiz_id
        return kwargs

    def post(self, request, *args, **wkwargs):
        quiz_id = self.kwargs.get("quiz_id")
        quiz_obj = get_object_or_404(Quiz, pk=quiz_id)
        try:
            selected_choice = request.POST['q1_selected']
            selected_choice2 = request.POST['q2_selected']
            selected_choice3 = request.POST['q3_selected']
            selected_choice4 = request.POST['q4_selected']
            selected_choice5 = request.POST['q5_selected']
        except(KeyError, Quiz.DoesNotExist):
            return render(request, 'quiz/votingError.html')
        else:
            quiz_obj.q1_selected = selected_choice
            quiz_obj.q2_selected = selected_choice2
            quiz_obj.q3_selected = selected_choice3
            quiz_obj.q4_selected = selected_choice4
            quiz_obj.q5_selected = selected_choice5
            quiz_obj.save()
            return HttpResponseRedirect(reverse('quiz:results', args=(quiz_id,)))


class ResultsView(DetailView):
    template_name = 'quiz/results.html'
    queryset = Quiz.objects.all()

    def get_object(self):
        quiz_id = self.kwargs.get("quiz_id")
        return get_object_or_404(Quiz, id=quiz_id)


# Does take you to the newly created page once completed
class AddView(CreateView):
    template_name = 'quiz/create.html'
    form_class = NewQuizForm
    queryset = QuizQuestion.objects.all()
    success_url = '../'

    def form_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)


class DeleteView(DeleteView):
    model = Quiz
    template_name = 'quiz/delete.html'
    success_url = '../../'


class EditView(UpdateView):
    model = NewQuizForm
    template_name = 'quiz/create.html'
    # form_class = QuizForm
    success_url = '../'

    def get_object(self):
        quiz_id = self.kwargs.get("quiz_id")
        return get_object_or_404(Quiz, id=quiz_id)
