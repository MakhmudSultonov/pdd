from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataAPIView

# router = DefaultRouter()
# router.register(r'data', DataViewSet)

urlpatterns = [
    path('data/', DataAPIView.as_view()),
]