from django.urls import path
from  . import  views

urlpatterns = [
    path('rooms', views.rooms_list, name="rooms"),
    path('<int:id>', views.detail, name="detail"),
]