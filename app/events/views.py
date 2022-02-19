from rest_framework import mixins, viewsets
from events.models import Session, Event
from events.serializers import SessionSerializer, EventSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from events.tasks import save_event_task


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

    def create(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = save_event_task.delay(request.data)
        return JsonResponse({"task_id": task.id}, status=202)
