# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from .serializers import SMSerializer
from .models import StaticMessages

@api_view(['GET', 'POST', 'DELETE'])
def messages_list(request):
    if request.method == 'GET':
        messages = StaticMessages.objects.all()
        messages_serializer = SMSerializer(messages, many=True)

        return JsonResponse(messages_serializer.data, safe=False)
