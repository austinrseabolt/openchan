from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('boards/<str:boardurl>/', views.board),
    path('boards/<str:boardurl>/<int:post_pk>/', views.ViewThread),
]