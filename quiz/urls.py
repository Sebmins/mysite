from django.urls import path
from .views import IndexView, AddView, DeleteView, QuizView, EditView

app_name = 'quiz'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:quiz_id>/', QuizView.as_view(), name='questionnaire'),
    path('<pk>/edit/', EditView.as_view(), name='edit',),
    path('<pk>/delete/', DeleteView.as_view(), name='delete'),
    path('create/', AddView.as_view(), name='create'),
]
