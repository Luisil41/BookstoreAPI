from django.urls import include, path, re_path
from . import views
from django.urls import re_path as url

urlpatterns = [
  path('welcome', views.welcome),
  path('getbooks', views.get_books),
  path('addbook', views.add_book),
  path('updatebook/<int:book_id>', views.update_book),
  path('deletebook/<int:book_id>', views.delete_book)
]