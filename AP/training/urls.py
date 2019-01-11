from django.conf.urls import url
from . import views
# from django.urls import path
# from django.contrib.auth.views import LoginView
# from training.views import Home, About, Calendar, Security, Professional_behaviour, Questions, Contact


urlpatterns = [
    # path('', views.Home),
    url(r'^$', views.Home, name='home'),
    url(r'^about/$', views.About, name='about' ),
    url(r'^calendar/$', views.EventView.as_view(), name='calendar'),
    url(r'^contact/$', views.Contact, name='contact'),
    url(r'^security/$', views.Security, name='videos'),
    url(r'^professional_behaviour/$', views.Professional_behaviour, name='videos'),
    url(r'^questions/$', views.Question, name='questions')
]
