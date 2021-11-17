from django.shortcuts import render

# Create your views here.
import json

from django.http     import JsonResponse
from django.views    import View
from django.db.models import Q
from .models import *


class ActorsView(View):
    def get(self, request):
        actors_data = Actor.objects.all()
        result_list = []

        for i in actors_data:
            b = Actors_movies.objects.filter(actor=i)
            result_list.append({
                "이름" : i.first_name,
                "성" : i.last_name,
                "출연영화" : [j.movie.title for j in b],
                
                })

            # 콘솔 확인용 for문, 1번은 정션테이블의 id, 2번은 movie 컬럼의 id이기 때문에 2번을 사용해야함!
            # for k in b:
            #     print(f"1번 j          = {k.movie}")
            #     print(f"2번 j.movie    = {k.movie}")
            #     print(f"3번 j.movie.id = {k.movie.id}")

        return JsonResponse({'result':result_list}, status=200)



class MoviesView(View):
    
    def get(self, request):
        
        movies_data = Movie.objects.all()
        result_list = []
        for i in movies_data:
            b = Actors_movies.objects.filter(movie=i)
            actor_list = []
            for j in b:
                actor_list.append({
                "성" : j.actor.last_name,
                "이름" : j.actor.first_name
                })
            result_list.append({
                "타이틀" : i.title,
                "러닝타임" : i.running_time,
                "출연배우" : actor_list
                })


        return JsonResponse({'result':result_list}, status=200)
