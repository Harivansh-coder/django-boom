from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from polls.views import home

urlpatterns = [
    path('', home, name= "home"),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]