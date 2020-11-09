from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, FormView, UpdateView

from .forms import VotingForm, CreateFormSet, EditFormSet, EditForm, QuestionForm, VotingForm2
from .models import Quiz, QuizQuestion


class IndexView(ListView):
    template_name = "quiz/index.html"
    queryset = Quiz.objects.all()
    # queryset = QuizQuestions.objects.order_by('-id').all()


class QuizView(FormView, DetailView):
    template_name = 'quiz/questionnaire.html'
    form_class = VotingForm2
    queryset = QuizQuestion.objects.all()
    success_url = '../'

    def get_object(self):
        quiz_id = self.kwargs.get("quiz_id")
        return get_object_or_404(Quiz, id=quiz_id)

    def get_form_kwargs(self):
        kwargs = super(QuizView, self).get_form_kwargs()
        quiz_id = QuizQuestion.objects.get(pk=self.kwargs["quiz_id"])
        question_id = QuizQuestion.objects.get(pk=self.kwargs["quiz_id"])
        kwargs['quiz'] = quiz_id
        return kwargs

    def post(self, request, *args, **wkwargs):
        quiz_id = self.kwargs.get("quiz_id")
        quiz_obj = get_object_or_404(Quiz, pk=quiz_id)
        question_id = QuizQuestion.objects.get(pk=self.kwargs["quiz_id"])
        print(quiz_id)
        print(quiz_obj)
        print(question_id)
        try:
            selected_option = int(request.POST['question_text'])
            args = {
                'selected': selected_option,
                'quiz': quiz_obj,
                'question': question_id
            }
            print(args)
        except(KeyError, Quiz.DoesNotExist):
            return render(request, 'quiz/votingError.html')
        else:
            quiz_obj.save()
            return TemplateResponse(request, 'quiz/results.html', args)


class ResultsView(DetailView):
    template_name = 'quiz/results.html'
    queryset = Quiz.objects.all()

    def get_object(self):
        quiz_id = self.kwargs.get("quiz_id")
        return get_object_or_404(Quiz, id=quiz_id)


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


# Doesn't save the QuizQuestions data
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


# class MultiView(View):
#
#     def get(self, request, quiz_id=None):
#         if quiz_id:
#             quiz = get_object_or_404(Quiz, id=quiz_id)
#             quiz_form = EditForm(instance=quiz)
#             question = quiz.quizquestion_set.all()
#             question_form = [QuestionForm(prefix=str(quiz.id), instance=q) for q in question]
#             template = 'quiz/edit.html'
#         else:
#             quiz_form = EditForm()
#             question_form = [QuestionForm(prefix=str(x),) for x in range(3)]
#             template = 'quiz/create.html'
#
#         context = {'quiz_form': quiz_form, 'question_form': question_form}
#         return render(request, template, context)
#
#     def post(self, request):
#         context = {}
#         quiz_form = EditForm(request.POST,) # instance=Quiz
#         question_form = [QuestionForm(request.POST, prefix=str(x),) for x in range(0, 3)] # instance=QuizQuestion
#         if quiz_form.is_valid() and all([q.is_valid() for q in question_form]):
#             new_quiz = quiz_form.save()
#             # new_quiz.id =
#             new_quiz.save()
#             for q in question_form:
#                 new_question = q.save()
#                 new_question.quiz = new_quiz
#                 new_question.save()
#             return HttpResponseRedirect('quiz/index.html')
#         context = {'quiz_form': quiz_form, 'question_form': question_form}
#         return render(request, 'quiz/create.html', context)
