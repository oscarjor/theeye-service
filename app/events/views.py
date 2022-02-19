from rest_framework import mixins, viewsets
from events.models import Session, Event
from events.serializers import SessionSerializer, EventSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class SessionsViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Viewset to Start a session in the eye
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SessionSerializer
    queryset = Session.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EventsViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Viewset to Create events records in the eye
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
