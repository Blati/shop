from django.urls import path

from .api_views import (
    CategoryAPIView,
    CustomersListAPIView,
    SmartphoneListAPIView,
    NotebookListAPIView,
    NotebookDetailAPIView,
    SmartphoneDetailAPIView
)

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='categories_list'),
    path('categories/<str:pk>/', CategoryAPIView.as_view(), name='category_upd'),
    path('customers/', CustomersListAPIView.as_view(), name='customers_list'),
    path('smartphones/', SmartphoneListAPIView.as_view(), name='smartphones_list'),
    path('notebooks/', NotebookListAPIView.as_view(), name='notebooks_list'),
    path('smartphones/<str:pk>/', SmartphoneDetailAPIView.as_view(), name='smartphone_detail'),
    path('notebooks/<str:pk>/', NotebookDetailAPIView.as_view(), name='notebook_detail')
]
