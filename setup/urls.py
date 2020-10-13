from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from scrapping.views import *

router = routers.DefaultRouter()
router.register('passing', PassingsViewSet, basename="Passings")
router.register('rushing', RushingsViewSet, basename="Rushing")
router.register('receiving', ReceivingsViewSet, basename="Receiving")
router.register('fumbles', FumblesViewSet, basename="Fumbles")
router.register('tackles', TacklesViewSet, basename="Tackles")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('import/', import_data),
    path('', include(router.urls)),
]