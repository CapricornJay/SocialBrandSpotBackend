# urls.py

from django.urls import path
from .views import CollaborationListCreateAPIView, CollaborationRequestListCreateAPIView, CollaborationRequestRetrieveUpdateDestroyAPIView, CollaborationRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('collaborations/', CollaborationListCreateAPIView.as_view(), name='collaboration-list-create'),
    path('collaborations/<int:pk>/', CollaborationRetrieveUpdateDestroyAPIView.as_view(), name='collaboration-retrieve-update-destroy'),
    path('collaboration-requests/', CollaborationRequestListCreateAPIView.as_view(), name='collaboration_request_list_create'),
    path('collaboration-requests/<int:pk>/', CollaborationRequestRetrieveUpdateDestroyAPIView.as_view(), name='collaboration_request_detail')
]
