from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"account/user", views.CustomUserViewSet)
router.register(r"account/group", views.GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
