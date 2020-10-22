from django.test import TestCase

from mainapp.api.serializers import CategorySerializer, SmartphoneSerializer
from mainapp.models import Category, Smartphone


class ShopSerializersTestCase(TestCase):

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

    def test_category_serializer(self):
        serializer_data = CategorySerializer([self.category1, self.category2], many=True).data
        expected_data = [
            {
                'id': self.category1.id,
                'name': 'KEKW',
                'slug': 'kekw'
            },
            {
                'id': self.category2.id,
                'name': 'KEKWait',
                'slug': 'kekwait'
            }
        ]
        self.assertEqual(expected_data, serializer_data)

    def test_smartphone_serializer(self):
        serializer_data = SmartphoneSerializer(self.smartphone1).data
        expected_data = {
                "id": self.smartphone1.id,
                "diagonal": "6",
                "display_type": "OLED",
                "resolution": "1792x828",
                "accum_volume": "3140",
                "ram": "16",
                "sd": True,
                "sd_volume_max": "128",
                "main_cam_mp": "12",
                "frontal_cam_mp": "8",
                "title": "Google Pixel 4a",
                "slug": "google-pixel-4a",
                "image": "/media/6hq_2.webp",
                "description": "Неважно",
                "price": "25000.00",
                "category": self.smartphone1.category.id
        }
        self.assertEqual(expected_data, serializer_data)
