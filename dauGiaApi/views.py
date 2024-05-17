from django.shortcuts import render
from django.http import HttpResponse
from  rest_framework.response import Response
from rest_framework import viewsets, permissions,serializers,status,generics
from .models import Post, Interact, User,Tag

from rest_framework.routers import DefaultRouter

from .serializers import PostSerializer, InteractSerializer,UserSerializer,UserDetailsSerializer, TagSerializer


# Create your views here.

def index(request):
    return HttpResponse("api")


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        # authentcate hay ko van cho xem
        if self.action == 'list':
            return [permissions.AllowAny()]
        #  aciton con lai bat buoc phair authenticated
        return [permissions.IsAuthenticated()]

class InteractViewSet(viewsets.ModelViewSet):
    queryset = Interact.objects.all()
    serializer_class = InteractSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    def create(self, request):
        # tạo dữ liệu từ post
        serializers = UserSerializer(data=request.data)
        if(serializers.is_valid()):
            # tạo dữ liệu người dùng mới
            user = User.objects.create_user(**serializers.validated_data)
            return Response({'message':'create user success'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


#genrics chỉ cho xem
class UserDetailViewsSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

