# serializers.py

from rest_framework import serializers
from .models import Influencer, Brand, Collaboration

from rest_framework import serializers
from .models import CollaborationRequest

class InfluencerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Influencer
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CollaborationSerializer(serializers.ModelSerializer):
    influencer = InfluencerSerializer()
    brand = BrandSerializer()

    class Meta:
        model = Collaboration
        fields = '__all__'

class CollaborationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaboration
        exclude = ['id']

class CollaborationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollaborationRequest
        fields = ('id', 'brand', 'influencer', 'message', 'created_at', 'updated_at')
        read_only_fields = ('id', 'status', 'created_at', 'updated_at')
