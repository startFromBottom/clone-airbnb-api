from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    # path("", views.rooms_view),
    path("", views.RoomsView.as_view()),
    path("<int:pk>/", views.RoomView.as_view()),
    path("search/", views.room_search),
]
