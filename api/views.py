from rest_framework.views import APIView
from rest_framework.response import Response
from api import serializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from api import models, permissions

class HelloApiView(APIView):
    serializer_class = serializer.HelloSerializer
    def get(self, request, format = None):
        an_apiview = [
            'APIView uses http method (Put, Patch, delete, get, post)',
            'manualy mapped to url',
            'gives full control',
            'best for application'
        ]
        return Response({'message': "Hello", 'an_apiview': an_apiview})
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST,
            )
    
    def delete(self, request, pk = None):
        return Response({'method': 'DELETE'})
    
    def put(self, request, pk = None):
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk = None):
        return Response({'method': 'PATCH'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializer.HelloSerializer
    def list(self, request):
        an_viewset = [
            'APIView uses http method (Put, Patch, delete, get, post)',
            'manualy mapped to url',
            'gives full control',
            'best for application'
        ]
        return Response({'message': "Hello", 'an_viewset': an_viewset})
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST,
            )
    
    def retrieve(self, request, pk = None):
        return Response({'method': 'GET'})
    
    def update(self, request, pk = None):
        return Response({'method': 'PUT'})
    
    def partial_update(self, request, pk = None):
        return Response({'method': 'PATCH'})
    
    def destroy(self, request, pk = None):
        return Response({'method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ProfileFeedViewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializer.ProfileFeedSerializer
    queryset = models.ProfileFeed.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(user_profile = self.request.user)