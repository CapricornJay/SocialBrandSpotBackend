from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Influencer
from .serializers import InfluencerSerializer

@api_view(['GET'])
def influencer_list(request):
    influencers = Influencer.objects.all()
    serializer = InfluencerSerializer(influencers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def influencer_create(request):
    serializer = InfluencerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def influencer_detail(request, pk):
    influencer = Influencer.objects.get(pk=pk)
    serializer = InfluencerSerializer(influencer)
    return Response(serializer.data)

@api_view(['PUT'])
def influencer_update(request, pk):
    influencer = Influencer.objects.get(pk=pk)
    serializer = InfluencerSerializer(instance=influencer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def influencer_delete(request, pk):
    influencer = Influencer.objects.get(pk=pk)
    influencer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)