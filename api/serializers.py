from rest_framework import serializers
from .models import Cancer
class CancerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cancer
        fields='__all__'