from rest_framework import serializers
from .models import Influencer


class InfluencerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Influencer
        fields = ('id', 'name', 'email', 'phone_number')
