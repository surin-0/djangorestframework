from django.db import models
from django.conf import settings

class Essay(models.Model) :
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete = models.CASCADE)
    # on_delete 필수
    # models.CASCADE : 모델을 지우면 지워짐
    title = models.CharField(max_length=30)
    body = models.TextField()

class Album(models.Model) :
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete = models.CASCADE)
    image = models.ImageField(upload_to= "images")
    desc = models.CharField(max_length=100)

class Files(models.Model) :
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete = models.CASCADE)
    myfile = models.FileField(blank=False, null=False, upload_to="files")
    desc = models.CharField(max_length=100)