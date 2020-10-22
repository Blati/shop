import json

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from  rest_framework import status

from mainapp.api.serializers import CategorySerializer, SmartphoneSerializer
from mainapp.models import Category, Smartphone


class ShopApiTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_username')
        self.staff = User.objects.create_superuser(username='staff_test_username', is_staff=True)
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

    def test_category_create_not_staff(self):
        self.assertEqual(2, Category.objects.all().count())
        url = reverse('categories_list')
        data = {
            "name": "Чайники",
            "slug": "teapots"
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(
            url, data=json_data,
            content_type='application/json'
        )
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.assertEqual(2, Category.objects.all().count())

    def test_category_create(self):
        self.assertEqual(2, Category.objects.all().count())
        url = reverse('categories_list')
        data = {
            "name": "Чайники",
            "slug": "teapots"
        }
        json_data = json.dumps(data)
        self.client.force_login(self.staff)
        response = self.client.post(
            url, data=json_data,
            content_type='application/json'
        )
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, Category.objects.all().count())

    def test_category_update_not_staff(self):
        url = reverse('category_upd', args=(self.category1.id,))
        data = {
            "name": 'Pepega',
            "slug": self.category1.slug
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(
            url, data=json_data,
            content_type='application/json'
        )
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.category1.refresh_from_db()
        self.assertEqual('KEKW', self.category1.name)

    def test_category_update(self):
        url = reverse('category_upd', args=(self.category1.id,))
        data = {
            "name": 'Pepega',
            "slug": self.category1.slug
        }
        json_data = json.dumps(data)
        self.client.force_login(self.staff)
        response = self.client.put(
            url, data=json_data,
            content_type='application/json'
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.category1.refresh_from_db()
        self.assertEqual('Pepega', self.category1.name)

    def test_smartphones_search(self):
        url = reverse('smartphones_list')
        response = self.client.get(url, data={'search': '25000'})
        serializer_data = SmartphoneSerializer(self.smartphone1).data
        serializer_data['image'] = 'http://testserver' + serializer_data['image']
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual([serializer_data], response.data)
