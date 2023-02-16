from django.urls import path
from .views import BrandListCreateAPIView, BrandRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('brands/', BrandListCreateAPIView.as_view(), name='brand-list-create'),
    path('brands/<int:pk>/', BrandRetrieveUpdateDestroyAPIView.as_view(), name='brand-retrieve-update-destroy'),
]
