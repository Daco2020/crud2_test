from django.shortcuts import render

# Create your views here.
import json

from django.http     import JsonResponse
from django.views    import View
from django.db.models import Q
from .models import *


class ActorsView(View):
    
    def get(self, request):
        actor_data = Actor.objects.all()
        result_list = []
        for i in actor_data:
            middle = i.movie.all()
            result_list.append({
                "성" : i.last_name,
                "이름" : i.first_name,
                "출연영화" : [j.title for j in middle]
                })
            
        return JsonResponse({'result':result_list}, status=200)



class MoviesView(View):
    
    # 오브젝트 가져오면 정션테이블 붙이고 올로 가져올 수 있음

    def get(self, request):
        
        
        movies_data = Movie.objects.all()
        result_list = []
        for i in movies_data:
            b = i.actor_set.all()
            print(f" b = {b}")
            actor_list = []
            for j in b:
                actor_list.append({
                "성" : j.last_name,
                "이름" : j.first_name
                })
                print(f" actor_list = {actor_list}")
            result_list.append({
                "타이틀" : i.title,
                "러닝타임" : i.running_time,
                "출연배우" : actor_list
                })


        return JsonResponse({'result':result_list}, status=200)
