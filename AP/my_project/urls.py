from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('loginpage/',include('loginpage.urls')),
    path('training/',include('training.urls')),
    url(r'^login/$', LoginView.as_view(template_name='loginpage/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='loginpage/login.html'), name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
