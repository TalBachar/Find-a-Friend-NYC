from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
	path('favorite', views.favorite, name='favorite'),
]
