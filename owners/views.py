# from django.shortcuts import render

# Create your views here.



import json

from django.http     import JsonResponse
from django.views    import View
from django.db.models import Q
from .models import Owner, Dog

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        Owner.objects.create(
            name  = data["name"],
            email = data["email"],
			age   = data["age"]
        )
        
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

    def get(self, request):
        data = json.loads(request.body)
        

        ## 1. if 로 or 식 만들기 -> 세 개 중에 하나만 들어와도 결과값을 반환해줌
        # if "name" in data:
        #     result = Owner.objects.filter(name=data["name"]).values('name','email','age')
        # elif "email" in data:
        #     result = Owner.objects.filter(email=data["email"]).values('name','email','age')
        # elif "age" in data:
        #     result = Owner.objects.filter(age=data["age"]).values('name','email','age')

        # 2-1. if와 Q() 를 이용해서 or 조건을 만들어서 작동
        age = -1
        email = -1
        name = -1
        if "age" in data:
            age = data["age"]
        if "email" in data:
            email = data["email"]
        if "name" in data:
            name = data["name"]

        # 2-2. or 조건문
        result = Owner.objects.filter(Q(age=age)|Q(email=email)|Q(name=name)).all()
        # dog_result = result.dog_set.filter(owner=result.id)
        dog_list = []
        n = 0
        owner_list = []
        for i in result:
            owner_list.append({
                "name" : i.name,
                "age" : i.age,
                "email" : i.email
                })
            dog_result = i.dog_set.all()
            # print(f"a :: {dog_result}")
            # print(f"dog list :: {dog_result.values('id', 'name')}")
            for j in dog_result:
                dog_list.append({
                    "dog_name" : j.name,
                    "dog_age" : j.age,
                    "owner_name" : j.owner.name
                    })
            # 오너에 대한 정보를 검색하면 강아지들이 함께 나오도록 하였다. 하지만 현재 for문으로는 오너를 여러명 조회할 경우 강아지 리스트가 오너의 수만큼 중복되어 나온다.                    


        # for i in dog_result:
        #     result_list.append({
        #         "name" : i.name,
        #         "age" : i.age,
        #         })
        return JsonResponse({'owner_result':owner_list, 'dog_result':dog_list}, status=200)


class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.get(name=data['owner'])
        
        Dog.objects.create(
            name    = data["name"],
            age     = data["age"],
            owner   = owner
        )

        return JsonResponse({'MESSAGE':'CREATED'}, status=201)
    
    def get(self, request):
        data = json.loads(request.body)
        # owner = Owner.objects.get(name=data['owner'])
        
        # 1. if 로 or 식 만들기 -> 세 개 중에 하나만 들어와도 결과값을 반환해줌    
        # if "name" in data:
        #     a = Dog.objects.filter(name=data["name"]).values('name', 'age')
        #     b = dict(a[0])
        #     b["owner"] = Dog.objects.get(name=data["name"]).owner.name
        #     result = b
            
        # elif "age" in data:
        #     a = Dog.objects.filter(age=data["age"]).values('name', 'age')
        #     b = dict(a[0])
        #     b["owner"] = Dog.objects.filter(age=data["age"])[0].owner.name
        #     result = b

        # elif "owner" in data:
        #     owner_id = Owner.objects.get(name=data["owner"])
        #     a = Dog.objects.filter(owner=owner_id)
        #     b = dict(a[0])
        #     b["owner"] = Dog.objects.get(owner=owner_id).owner.name
        #     result = b
        # return JsonResponse({'result':result_list}, status=200)

        # 2-1 
        age = -1
        owner = -1
        name = -1
        if "age" in data:
            age = data["age"]
        if "owner" in data:
            owner = data["owner"]
        if "name" in data:
            name = data["name"]

        # 오너의 이름을 불러와 인풋의 오너 이름과 일치하는지 확인해야 함
        # owner_id = Owner.objects.get(name=data["owner"])

        # 2-2. or 조건문
        
        result = Dog.objects.filter(Q(age=age)|Q(name=name)|Q(owner=owner)).all()
        result_list = []
        for i in result:
            result_list.append({
                "name" : i.name,
                "age" : i.age,
                "owner_name" : i.owner.name,
            })

        return JsonResponse({'result':result_list}, status=200)


        # for len(range())
        # for 