from django.contrib import admin
from django.urls import path, include
from .serializers import PostSerializer
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)
router.register('comment', views.InteractViewSet)
router.register('user',views.UserViewSet,basename='user')
router.register('userDetail',views.UserDetailViewsSet,basename='user-detail')
router.register('tag',views.TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
