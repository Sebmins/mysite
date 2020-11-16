from django.db import transaction
from django.shortcuts import get_object_or_404, render
from django.template.response import TemplateResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, FormView, UpdateView
from .forms import VotingForm, CreateFormSet, EditFormSet
from .models import Quiz, QuizQuestion


class IndexView(ListView):
    template_name = "quiz/index.html"
    queryset = Quiz.objects.all()


class QuizView(FormView, DetailView):
    template_name = 'quiz/questionnaire.html'
    form_class = VotingForm
    queryset = QuizQuestion.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = QuizQuestion.objects.filter(quiz=self.kwargs["quiz_id"]).values()
        context['question'] = list(question)
        return context

    def get_form_kwargs(self):
        kwargs = super(QuizView, self).get_form_kwargs()
        quiz_id = QuizQuestion.objects.filter(quiz=self.kwargs["quiz_id"])
        kwargs['quiz'] = quiz_id
        return kwargs

    def get_object(self):
        quiz_id = self.kwargs.get("quiz_id")
        return get_object_or_404(Quiz, id=quiz_id)


class ResultsView(DetailView):
    template_name = 'quiz/results.html'
    queryset = Quiz.objects.all()

    def get_object(self):
        quiz_id = self.kwargs.get("quiz_id")
        return get_object_or_404(Quiz, id=quiz_id)

    def post(self, request, *args, **wkwargs):
        quiz_obj = get_object_or_404(Quiz, pk=self.kwargs.get("quiz_id"))
        question = QuizQuestion.objects.filter(quiz=self.kwargs["quiz_id"])

        selected_answers = []
        try:
            for i in range(question.count()):
                selected_answers.append(int(request.POST['question_text'+str(i)]))

            args = {
                'answer_object': zip(selected_answers, question),
                'quiz': quiz_obj,
            }

        except(KeyError, Quiz.DoesNotExist):
            return render(request, 'quiz/votingError.html')
        else:
            quiz_obj.save()
            return TemplateResponse(request, 'quiz/results.html', args)


# Does take you to the newly created page once completed
class AddView(CreateView):
    model = Quiz
    fields = '__all__'
    success_url = '../'
    template_name = 'quiz/create.html'

    def get_context_data(self, **kwargs):
        data = super(AddView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['quizquestion'] = CreateFormSet(self.request.POST)
        else:
            data['quizquestion'] = CreateFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        quizquestion = context['quizquestion']
        with transaction.atomic():
            self.object = form.save()

            if quizquestion.is_valid():
                quizquestion.instance = self.object
                quizquestion.save()
        return super(AddView, self).form_valid(form)


class DeleteView(DeleteView):
    model = Quiz
    template_name = 'quiz/delete.html'
    success_url = '../../'


class EditView(UpdateView):
    model = Quiz
    fields = '__all__'
    template_name = 'quiz/edit.html'
    success_url = '../'

    def get_context_data(self, **kwargs):
        data = super(EditView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['quizquestion'] = EditFormSet(self.request.POST, instance=self.object)
        else:
            data['quizquestion'] = EditFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        quizquestion = context['quizquestion']

        with transaction.atomic():
            self.object = form.save()

            if quizquestion.is_valid():
                quizquestion.instance = self.object
                quizquestion.save()
        return super(EditView, self).form_valid(form)
