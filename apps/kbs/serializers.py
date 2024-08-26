from rest_framework import serializers
from .models import Keyboard, Button

class ButtonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Button
        fields = '__all__'

class KbSerializer(serializers.ModelSerializer):
    buttons = ButtonSerializer(many=True, read_only=True)
    class Meta:
        model = Keyboard
        fields = '__all__'


