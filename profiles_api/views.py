from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelleSerializer

    def get(self, request, format=None):
        """This function return a list of APIView features"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is simmilar to a traditional Django View',
            'gives you the most control over your application logic',
            'is mapped manually to ULS',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a Hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """handle updating an objects """
        return Response({'method': 'PUT'})


    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})