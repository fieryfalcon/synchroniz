from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from .views import ExchangeTokenView
# from agora.views import VideoChatRoomViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register("app_user", views.app_user_modelviewset, basename="app user")
router.register("note", views.note_viewset, basename="note")
router.register("task", views.task_viewset, basename="task")
# router.register(r'rooms', VideoChatRoomViewSet, basename='room')

urlpatterns = [
    path("api_view/", include(router.urls)),
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('exchange-token/', ExchangeTokenView.as_view(), name='exchange-token'),
    # path('rooms/<int:pk>/join/',
    #      VideoChatRoomViewSet.as_view({'post': 'join_room'})),
]
