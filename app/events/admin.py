from django.contrib import admin
from events.models import Application, Session, EventCategory, Event

admin.site.register(Application)
admin.site.register(Session)
admin.site.register(EventCategory)
admin.site.register(Event)
