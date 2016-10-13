from django.conf.urls import url, include

from rest_framework import routers

from todo.api import viewsets


router = routers.DefaultRouter()
router.register(r'list', viewsets.ListViewSet, 'list')
router.register(r'item', viewsets.ItemViewSet, 'item')


urlpatterns = [
    url(r'', include(router.urls))
]
