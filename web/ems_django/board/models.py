from django.db import models

# Create your models here.
# python manage.py makemigrations
# python manage.py migrate
class Board(models.Model):
    # num : 값이 없으면 자동으로 증가
    num = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    pw = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    regdate = models.DateTimeField(null=True)
    readcnt = models.IntegerField(default=0)
    file1 = models.CharField(max_length=300)
    
    def __str__(self):
        return str(self.num) + ":" + self.title