from .models import Posts
from .serializers import PostSerializers
from rest_framework import viewsets,permissions

class PostViewset(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers
    permission_classes = [
        permissions.IsAuthenticated
    ]

