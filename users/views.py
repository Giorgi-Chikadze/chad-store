from rest_framework import mixins, viewsets
from django.contrib.auth import get_user_model
from users.serializers import RegisterSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.permissions import IsObjectOwnerOrReadOnly
from django.core.exceptions import PermissionDenied
from rest_framework.decorators import action
from rest_framework.response import Response

User = get_user_model()

class UserListDetailViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin ,viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)



class RegisterView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer



class ProfileViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsObjectOwnerOrReadOnly]
    serializer_class = ProfileSerializer




