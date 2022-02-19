import json

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from events.models import Application, Session, EventCategory, Event


class EventsTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user("test_website_user")
        user.set_password('admin123')
        user.save()
        self.token = Token.objects.create(user=user)
        self.app = Application.objects.create(name="Test Website", slug="test_website", user=user)
        self.category = EventCategory.objects.create(name="Website Page Interaction", slug="page interaction")
        self.session = Session.objects.create(application=self.app, metadata={})

    def test_session_creation(self):
        """
        Test session creation
        """
        client = APIClient()
        response = client.post(
            '/api/sessions/', {
                'application': self.app.slug,
                'metadata': {},
            },
            format='json',
            **{'HTTP_AUTHORIZATION': f'Token {str(self.token)}'},
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        result = json.loads(response.content)
        self.assertIn('session_id', result)

    def test_events_creation(self):
        """
        Test events creation
        """
        client = APIClient()
        response = client.post(
            '/api/events/', {
                'session': self.session.session_id,
                'category': 'page interaction',
                'name': 'cta click',
                'data': {
                    'host': 'www.consumeraffairs.com',
                    'path': '/',
                    'element': 'chat bubble'
                },
                'timestamp': '2021-01-01 09:15:27.243860'
            },
            format='json',
            **{'HTTP_AUTHORIZATION': f'Token {str(self.token)}'},
        )

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
