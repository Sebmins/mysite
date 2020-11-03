from django.urls import path
from . import views
from .views import IndexView, ResultsView, AddView, DeleteView, QuizView, EditView

# from .views import product_create_view, render_initial_data, delete_data, IndexView

app_name = 'quiz'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:question_id>/', QuizView.as_view(), name='questionnaire'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/edit/', EditView.as_view(), name='edit',),
    path('<pk>/delete/', DeleteView.as_view(), name='delete'),
    path('create/', AddView.as_view(), name='create'),
]
