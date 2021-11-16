from django.db import models

# Create your models here.




class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=300)
    age = models.IntegerField()

    class Meta:
        db_table = 'owners'


class Dog(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField(default="알 수 없음", blank=True)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)

    class Meta:
        db_table = 'dogs'



