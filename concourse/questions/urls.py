from django.urls import path
from .views import QuestionView, RoundsView, congo_view


urlpatterns = [
	path('questions/', QuestionView.as_view(), name='questions'),
    path('rounds/', RoundsView.as_view(), name='rounds'),
    path('congratulations/', congo_view, name='congo'),
]