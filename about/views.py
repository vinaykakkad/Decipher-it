from django.shortcuts import render

from .models import Events

def about_view(request, *args, **kwargs):
	context = {}
	return render(request, 'about/about.html', context)

def event_list_view(request, *args, **kwargs):
	event_list = Events.objects.all()
	
	context = {'event_list': event_list}
	return render(request, 'about/event.html', context)

def event_detail_view(request, slug, *args, **kwargs):
	event = Events.objects.get(slug=slug)

	context = {'object': event}
	return render(request, 'about/event_detail.html', context)