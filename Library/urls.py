from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Library.views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('books/', books_list, name='books_list'),
    path('notready/', not_ready, name='not_ready'),
    path('books/<int:book_id>/', book_detail, name='book'),

]