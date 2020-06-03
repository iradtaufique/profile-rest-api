from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """This function return a list of APIView features"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is simmilar to a traditional Django View',
            'gives you the most control over your application logic',
            'is mapped manually to ULS',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

