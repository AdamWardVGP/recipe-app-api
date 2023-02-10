"""
tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import User

class ModelTests(TestCase):
    """Test models."""

    def test_creat_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Validate that we've normalized new users email addresses"""
        # source email to result
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@example.com', 'Test2@example.com'],
            ['TEST3@example.com', 'TEST3@example.com'],
            ['test4@example.com', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=email
            )
            self.assertEquals(expected,user.email)
    
    def test_new_user_requires_email(self):
        """Validate that creating a user without an email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test the creation of a superuser"""
        email = 'supertest@example.com'
        password = 'testpass123'
        user: User = get_user_model().objects.create_superuser(
            email = email,
            password = password
        )
        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)