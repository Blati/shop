from _collections import OrderedDict

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from .serializers import CategorySerializer, SmartphoneSerializer, NotebookSerializer, CustomerSerializer
from ..models import Category, Smartphone, Notebook, Customer


class CategoryPagination(PageNumberPagination):

    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('Всего объектов', self.page.paginator.count),
            ('Следующая', self.get_next_link()),
            ('Предыдущая', self.get_previous_link()),
            ('Результаты', data)
        ]))


class CategoryAPIView(ListCreateAPIView, RetrieveUpdateAPIView):

    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    queryset = Category.objects.get_queryset().order_by('id')
    permission_classes = [IsAuthenticatedOrReadOnly]


class SmartphoneListAPIView(ListAPIView):

    serializer_class = SmartphoneSerializer
    queryset = Smartphone.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']


class NotebookListAPIView(ListAPIView):

    serializer_class = NotebookSerializer
    queryset = Notebook.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']


class SmartphoneDetailAPIView(RetrieveAPIView):

    serializer_class = SmartphoneSerializer
    queryset = Smartphone.objects.all()


class NotebookDetailAPIView(RetrieveAPIView):

    serializer_class = NotebookSerializer
    queryset = Notebook.objects.all()


class CustomersListAPIView(ListAPIView):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
