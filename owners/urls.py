from django.urls import path

from .views import *

urlpatterns = [
	path('', OwnersView.as_view()),
    path('dogs', DogsView.as_view())
]