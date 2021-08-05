from django.urls import path, include
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('profile', Profile.as_view(), name='index'),
    path('about', About.as_view(), name='index'),
    path('menu', Menu.as_view(), name='index'),
    path('coffee', Coffee.as_view(), name='index'),
    path('account/regular', Regular.as_view(), name='index'),
    path('order', Order.as_view(), name='index'),
    path('product/<product>', Products.as_view(), name='product'),
]