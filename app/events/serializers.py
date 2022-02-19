from rest_framework import serializers
from events.models import Session, Event, Application, EventCategory


class SessionSerializer(serializers.ModelSerializer):
    """
    Serializer for sessions creation
    """
    application = serializers.SlugRelatedField(queryset=Application.objects.all(), slug_field='slug')
    metadata = serializers.JSONField()

    class Meta:
        model = Session
        fields = ['application', 'metadata', 'session_id', 'timestamp']


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for events creation
    """
    session = serializers.SlugRelatedField(queryset=Session.objects.all(), slug_field='session_id')
    category = serializers.SlugRelatedField(queryset=EventCategory.objects.all(), slug_field='slug')
    name = serializers.CharField(max_length=100)
    data = serializers.JSONField()

    class Meta:
        model = Event
        fields = ['session', 'category', 'name', 'data', 'timestamp']
