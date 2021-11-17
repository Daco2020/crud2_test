from django.urls import path

from .views import *

urlpatterns = [
	path('actors', ActorsView.as_view()),
    path('', MoviesView.as_view())
]