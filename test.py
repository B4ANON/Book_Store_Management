from django.test import TestCase
from bookstoremanagement.models import Book


# Create your tests here.

class UserTestCase(TestCase):
    def test_user(self):
        if len(Book.objects.all())>0:
            print(len(Book.objects.all()))
        return True