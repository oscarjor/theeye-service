from rest_framework import serializers
from events.models import Session, Event, Application, EventCategory
from events.utils import VALIDATOR_MAP
from django.utils import timezone


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

    def validate(self, data):
        """
        Check specific validation based on category and name and validate no future dates.
        """
        if data['timestamp'] > timezone.now():
            raise serializers.ValidationError("timestamp should not be in the future")

        validation_key = f"{data['category'].slug} : {data['name']}"
        print(">>>>>", validation_key)
        if validation_key in VALIDATOR_MAP:
            keys = VALIDATOR_MAP.get(validation_key)
            for key in keys:
                if key not in data['data'].keys():
                    raise serializers.ValidationError("the data payload is not valid for the category and name")
        return data
