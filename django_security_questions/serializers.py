from .models import SecurityQuestion, SecurityAnswer
from rest_framework import serializers

class SecurityQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityQuestion
        fields = '__all__'


class SecurityAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityAnswer
        fields = '__all__'

