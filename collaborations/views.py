# views.py

from rest_framework import generics
from .models import Influencer, Brand, Collaboration
from .serializers import InfluencerSerializer, BrandSerializer, CollaborationSerializer, CollaborationCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CollaborationRequest
from .serializers import CollaborationRequestSerializer

class CollaborationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Collaboration.objects.all()
    serializer_class = CollaborationSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CollaborationCreateSerializer
        return CollaborationSerializer

class CollaborationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collaboration.objects.all()
    serializer_class = CollaborationSerializer


class CollaborationRequestListCreateAPIView(generics.ListCreateAPIView):
    queryset = CollaborationRequest.objects.all()
    serializer_class = CollaborationRequestSerializer


class CollaborationRequestRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CollaborationRequest.objects.all()
    serializer_class = CollaborationRequestSerializer
