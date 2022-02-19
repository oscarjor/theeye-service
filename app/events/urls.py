from django.urls import include, path
from rest_framework import routers
from events import views

router = routers.DefaultRouter()
router.register(r'sessions', views.SessionsViewSet)
router.register(r'events', views.EventsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
