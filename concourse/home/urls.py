from django.urls import path

from .views import (home_page_view, leaderboard_view, 
					instruction_view, about_view)


urlpatterns = [
	path('', home_page_view, name='home'),
	path('leaderboard/', leaderboard_view, name='leaderboard'),
	path('instructions/', instruction_view, name='instructions'),
	path('about/', about_view, name='about'),
]