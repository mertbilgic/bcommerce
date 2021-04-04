from django.urls import path,re_path

from .views import home,HomeView

urlpatterns = [
    path('mockhome/',home, name='mockhome'),
    path('',HomeView.as_view(),name='home')
]
