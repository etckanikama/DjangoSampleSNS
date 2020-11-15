from django.db import models

# Create your models here.

class BoardModel(models.Model):
    titile = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    # 画像をuploadする機能
    image = models.ImageField(upload_to='')
    good = models.IntegerField()
    read = models.IntegerField()
    readtext = models.CharField(max_length=100)
