from rest_framework import serializers
from .models import Keyboard, Button

class KbSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keyboard
        fields = '__all__'

class ButtonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Button
        fields = '__all__'


