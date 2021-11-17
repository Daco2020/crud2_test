from django.urls import path

from .views import *

urlpatterns = [
	path('', ActorsView.as_view()),
    path('', MoviesView.as_view())
]