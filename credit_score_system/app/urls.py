from django.urls import path
from . import views

urlpatterns = [
    path('', views.questions_view, name='questions'),
    path('submit-answers/', views.submit_answers, name='submit_answers'),
    path('results/', views.results_view, name='results'),
]
