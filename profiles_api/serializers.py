from rest_framework import serializers
"""serializer function very simmilar to django form"""


class HelleSerializer(serializers.Serializer):
    """serialize a name field for testing aur API"""
    name = serializers.CharField(max_length=10)
