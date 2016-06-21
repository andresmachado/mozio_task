from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'providers', views.ProviderViewSet)
router.register(r'polygons', views.PolygonViewSet, base_name='Polygon')

urlpatterns = [
    url(r'^', include(router.urls)),
]
