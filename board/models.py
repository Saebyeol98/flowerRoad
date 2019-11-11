from django.db import models
from django.utils import timezone
from members.models import User

# Create your models here.


class BoardData(models.Model):
    board_number = models.AutoField(null=False, primary_key=True)
    board_title = models.CharField(max_length = 126, null=False)
    board_content = models.TextField(null=False)
    board_writer = models.ForeignKey(User, on_delete=models.CASCADE)
    board_date = models.CharField(max_length=140)
    #ssss
    
    def __str__(self):
        return super().__str__()
