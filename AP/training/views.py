from django.shortcuts import render
from django.views import View
from .models import *
from django.views.generic import TemplateView


def About(request):
    return render(request, 'training/about.html')


def Home(request):
    return render(request, 'training/home.html')


def Security(request):
    return render(request, 'training/videos.html')


def Professional_behaviour(request):
    return render(request, 'training/videos.html')


def Contact(request):
    return render(request, 'training/contact.html')


# def Calendar(request):
#     return render(request, 'training/calendar.html')


def Question(request):
    return render(request, 'training/questions.html')

class EventView(TemplateView):
	template_name = 'training/calendar.html'

	def get_context_data(self,**kwargs):
		query = Event.objects.all()		
		context={'form':query}
		return context
