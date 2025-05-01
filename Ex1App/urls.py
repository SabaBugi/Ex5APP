from django.urls import path
from . import views
from .views import user_registration_view, category_view

urlpatterns = [
    path('', views.home_view, name='home'),
    path('user_registration/', user_registration_view, name='user_registration'),
    path('category/', category_view, name='category'),
]

