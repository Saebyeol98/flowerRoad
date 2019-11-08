from django.db import models
from django.utils import timezone
from members.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField('제목', max_length=126, null=False)
    content = models.TextField('내용', null=False)
    number = models.AutoField(null=False,primary_key=True)
    author = models.CharField('작성자',max_length=16,null=False)
    created_at = models.DateTimeField('작성일')
    userid = models.ForeignKey(User,on_delete=models.CASCADE,)

    def __str__(self):
        return self.title
    
