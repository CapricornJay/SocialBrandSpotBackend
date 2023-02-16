from django.urls import path
from . import views

urlpatterns = [
    path('influencers/', views.influencer_list, name='influencer_list'),
    path('influencers/<int:pk>/', views.influencer_detail, name='influencer_detail'),
    path('influencers/new/', views.influencer_create, name='influencer_create'),
    path('influencers/<int:pk>/edit/', views.influencer_update, name='influencer_update'),
    path('influencers/<int:pk>/delete/', views.influencer_delete, name='influencer_delete'),
]
