from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from api.views import Demo_viewset


router = routers.SimpleRouter()
router.register(r'users', Demo_viewset,basename = "ssfg")
urlpatterns = router.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include(router.urls))
]
