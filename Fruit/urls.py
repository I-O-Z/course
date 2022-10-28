from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Fruit.views import *

urlpatterns = [
    path('', index_template, name='index_Fruit'),
    path('list/', fruit_template, name='list_fruit'),
    path('httpresponse/', index),
    path('add/', fruit_add, name='add_fruit'),
    path('list/<int:fruit_id>/', fruit_detail, name='one_fruit'),
    path('info/', request_info)
]



