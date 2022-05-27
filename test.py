from django.test import TestCase
from bookstoremanagement.models import Book


# Create your tests here.

class UserTestCase(TestCase):
    def test_user(self):
        booklist = Book.objects.filter(book_title="Python for Everybody")
        if booklist.book_title+1==0:    
            print("success")
        return True