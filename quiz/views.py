from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import QuizQuestions, Answer


def index(request):
    latest_question_list = QuizQuestions.objects.order_by('-name')[:5]
    template = loader.get_template('quiz/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'quiz/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(QuizQuestions, pk=question_id)
    return render(request, 'quiz/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(QuizQuestions, pk=question_id)
    return render(request, 'quiz/results.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Answer
    template_name = 'quiz/results.html'


def vote(request, question_id):
    question = get_object_or_404(QuizQuestions, pk=question_id)
    try:
        selected_choice = request.POST['group1']
        selected_choice2 = request.POST['group2']
        selected_choice3 = request.POST['group3']
        selected_choice4 = request.POST['group4']
        selected_choice5 = request.POST['group5']
    except(KeyError, QuizQuestions.DoesNotExist):
        return render(request, 'quiz/votingError.html')
    else:
        question.q1_selected = selected_choice
        question.q2_selected = selected_choice2
        question.q3_selected = selected_choice3
        question.q4_selected = selected_choice4
        question.q5_selected = selected_choice5
        print("selected = ", selected_choice)
        print("selected = ", selected_choice2)
        question.save()
        return HttpResponseRedirect(reverse('quiz:results', args=(question_id,)))
