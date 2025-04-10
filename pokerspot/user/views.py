from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generar token JWT
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'User created succesfuly',
                'username': user.username,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)