from rest_framework.generics import ListAPIView
from rest_framework import permissions
from .serializers import UserSerializer
from .permissions import IsAdmin
from .models import User


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
