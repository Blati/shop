from django.urls import reverse

from rest_framework.test import APITestCase
from  rest_framework import status

from mainapp.api.serializers import CategorySerializer, SmartphoneSerializer
from mainapp.models import Category, Smartphone


class ShopApiTestCase(APITestCase):

    def setUp(self):
        self.category1 = Category.objects.create(name='KEKW', slug='kekw')
        self.category2 = Category.objects.create(name='KEKWait', slug='kekwait')
        self.smartphone1 = Smartphone.objects.create(
            diagonal='6',
            display_type='OLED',
            resolution='1792x828',
            accum_volume='3140',
            ram='16',
            sd=True,
            sd_volume_max='128',
            main_cam_mp='12',
            frontal_cam_mp='8',
            title='Google Pixel 4a',
            slug='google-pixel-4a',
            image='6hq_2.webp',
            description='Неважно',
            price=25000.00,
            category=self.category1
        )

    def test_categories(self):
        url = reverse('categories_list')
        response = self.client.get(url)
        serializer_data = CategorySerializer([self.category1, self.category2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data[next(reversed(response.data))])

    def test_smartphones_search(self):
        url = reverse('smartphones_list')
        response = self.client.get(url, data={'search': '25000'})
        serializer_data = SmartphoneSerializer(self.smartphone1).data
        serializer_data['image'] = 'http://testserver' + serializer_data['image']
        self.assertEqual([serializer_data], response.data)
