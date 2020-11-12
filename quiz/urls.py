from django.urls import path
from .views import IndexView, AddView, ResultsView, DeleteView, QuizView, EditView

app_name = 'quiz'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:quiz_id>/', QuizView.as_view(), name='questionnaire'),
    path('<int:quiz_id>/results/', ResultsView.as_view(), name='results'),
    path('<pk>/edit/', EditView.as_view(), name='edit',),
    path('<pk>/delete/', DeleteView.as_view(), name='delete'),
    path('create/', AddView.as_view(), name='create'),
]
