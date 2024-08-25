from rest_framework import serializers
from .models import StaticMessages, UserStatus, State, Trigger
from apps.kbs.serializers import KbSerializer

class USSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserStatus
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'

class TriggerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trigger
        fields = '__all__'

class SMSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)
    user_status = USSerializer(read_only=True)
    trigger = TriggerSerializer(read_only=True)
    keyboard = KbSerializer(read_only=True)

    class Meta:
        model = StaticMessages
        fields = '__all__'
