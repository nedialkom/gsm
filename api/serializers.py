from rest_framework import serializers
from api.models import Phone

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['phoneHash', 'rating', 'created']