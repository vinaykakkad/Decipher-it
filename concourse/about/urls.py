from django.urls import path

from .views import event_list_view, event_detail_view, about_view

urlpatterns = [
    # path('about/', about_view, name='about'),
    # path('event/', event_list_view, name='event'),
    # path('event/<slug:slug>/', event_detail_view, name='event_detail'),
]