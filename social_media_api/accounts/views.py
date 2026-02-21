from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()

    def post(self, request, user_id):
        user_to_follow = self.get_queryset().get(id=user_id)
        if user_to_follow == request.user:
            return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(user_to_follow)
        return Response({'message': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()

    def post(self, request, user_id):
        user_to_unfollow = self.get_queryset().get(id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({'message': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)
