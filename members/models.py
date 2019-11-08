from django.db import models

# Create your models here.
class User(models.Model):
    userid=models.CharField(max_length=20, primary_key=True)
    userpw=models.CharField(max_length=20)
    phone_num=models.CharField(max_length=30)
    birth_date=models.DateField()
    addr=models.TextField()
    gender=models.CharField(max_length=20)
    email=models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.userid