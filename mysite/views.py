from django.http import HttpResponse
from django.views import generic


class HomeView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet
        """
        return "hi"


