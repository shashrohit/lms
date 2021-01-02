from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list books')
        self.detail_url = reverse('book details')

    def test_list_available_books(self):

        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('list_books.html')

    def test_book_details(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 201)
        self.assertTemplateUsed('book_details.html')


