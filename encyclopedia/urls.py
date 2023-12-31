from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name="home"),
    path('create_page/', create_page, name="create"),
    path('all_pages/', all_pages, name="all"),
    path('detail_page/<str:slug>/', detail_page, name="detail"),
    path('edit_page/<int:page_id>/', edit_page, name="edit"),
    path('delete_page/<int:page_id>/', delete_page, name="delete"),
    path('random_page/', random_page, name='random'),
]