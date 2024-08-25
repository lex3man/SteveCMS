# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from .serializers import SMSerializer
from .models import StaticMessages, State

@api_view(['GET'])
def all_messages_list(request):
    messages = StaticMessages.objects.all()
    messages_serializer = SMSerializer(messages, many=True)
    return JsonResponse(messages_serializer.data, safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def state_messages_list(request, state):
    if request.method == 'GET':
        state = State.objects.filter(caption=state).first()
        messages = StaticMessages.objects.filter(state=state).all()
        messages_serializer = SMSerializer(messages, many=True)
        return JsonResponse(messages_serializer.data, safe=False)
