from django.urls import reverse

from rest_framework.test import APITestCase
from  rest_framework import status

from mainapp.api.serializers import CategorySerializer
from mainapp.models import Category


class ShopApiTestCase(APITestCase):

    def test_categories(self):
        category1 = Category.objects.create(name='KEKW', slug='kekw')
        category2 = Category.objects.create(name='KEKWait', slug='kekwait')
        url = reverse('categories_list')
        response = self.client.get(url)
        serializer_data = CategorySerializer([category1, category2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data[next(reversed(response.data))])

