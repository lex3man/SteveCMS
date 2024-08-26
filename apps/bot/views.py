# from django.shortcuts import render
from rest_framework.decorators import api_view

from django.http.response import JsonResponse

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
        try:
            all_state = State.objects.get(caption="all")
            messages_for_all = StaticMessages.objects.filter(state=all_state).all()
            messages = messages.union(messages_for_all)
        except: pass
        messages_serializer = SMSerializer(messages, many=True)
        return JsonResponse(messages_serializer.data, safe=False)
