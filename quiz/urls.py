from django.urls import path
from . import views
from .views import IndexView, ResultsView, AddView, DeleteView, QuizView

# from .views import product_create_view, render_initial_data, delete_data, IndexView

app_name = 'quiz'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:question_id>/', QuizView.as_view(), name='questionnaire'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/edit/', views.editView, name='edit',),
    path('<int:question_id>/delete/', views.deleteView, name='delete'),
    path('create/', AddView.as_view(), name='create'),
]
