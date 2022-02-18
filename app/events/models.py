import uuid
from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="User that owns the app")
    name = models.CharField(max_length=30, help_text="Name of the app")
    slug = models.CharField(max_length=20, help_text="Slug of the app", unique=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE,
                                    help_text="Application that creates the session")
    session_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,
                                  help_text="Public session identifier")
    timestamp = models.DateTimeField(auto_now_add=True, help_text="Session creation timestamp")
    metadata = models.JSONField(blank=True, null=True, help_text="Optional metadata for the session")

    def __str__(self):
        return f"{self.application.name} - {self.session_id}"


class EventCategory(models.Model):
    slug = models.CharField(max_length=50, unique=True, help_text="Event category slug to identify the category")
    name = models.CharField(max_length=100, help_text="Category name")

    def __str__(self):
        return f"{self.slug} - {self.name}"


class Event(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, help_text="Session related to event")
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, help_text="Category related to event")
    name = models.CharField(max_length=100, help_text="Event name")
    data = models.JSONField(help_text="Data required for the event")
    timestamp = models.DateTimeField(help_text="Event creation timestamp")

    def __str__(self):
        return f"{self.session.session_id} - {self.category.name} - {self.name}"
