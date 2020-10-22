from django.test import TestCase

from mainapp.api.serializers import CategorySerializer
from mainapp.models import Category


class ShopSerializersTestCase(TestCase):

    def test_category_serializer(self):
        category1 = Category.objects.create(name='KEKW', slug='kekw')
        category2 = Category.objects.create(name='KEKWait', slug='kekwait')
        serializer_data = CategorySerializer([category1, category2], many=True).data
        expected_data = [
            {
                'id': 1,
                'name': 'KEKW',
                'slug': 'kekw'
            },
            {
                'id': 2,
                'name': 'KEKWait',
                'slug': 'kekwait'
            }
        ]
        self.assertEqual(expected_data, serializer_data)
