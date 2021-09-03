# myapp/urls.py

from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create_view, name='create'),
    path('logout/', logout_view, name='logout'),
    path('delete/', delete_view, name='delete'),
]