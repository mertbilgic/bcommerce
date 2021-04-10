from django.urls import path

from .views import ProductDetail

urlpatterns = [
    path('product/<slug>/',ProductDetail.as_view(),name='product')
]
