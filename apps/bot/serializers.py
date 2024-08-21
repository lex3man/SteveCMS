from rest_framework import serializers
from .models import StaticMessages

class SMSerializer(serializers.ModelSerializer):

    class Meta:
        model = StaticMessages
        fields = '__all__'
