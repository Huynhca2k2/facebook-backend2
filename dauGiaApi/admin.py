from django.contrib import admin
from  .models import Post, Interact,User

# Register your models here.

admin.site.register(Post)
admin.site.register(Interact)
admin.site.register(User)
