from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    img = models.ImageField(upload_to='post/%Y/%m', default=None)  # tự động tạo đường dẫn theo năm và ngày
    post = models.CharField(max_length=255)
    minPrice = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag',blank=True, null=True)


# Tương tác với post
class Interact(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    like = models.BooleanField(default=False)

class Tag(models.Model):
    name = models.CharField(max_length=50)

