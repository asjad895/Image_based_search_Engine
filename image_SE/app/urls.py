from django.urls import path
from .import views

urlpatterns = [
    path('',views.search,name='index'),
    path('api/search/', views.search, name='search'),
    path('api/results/', views.results, name='results'),
    path('api/home/', views.search, name='home'),
]
