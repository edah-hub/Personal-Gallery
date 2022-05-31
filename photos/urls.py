from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='homepage'),
  path('categories/', views.categories, name='category-list'),
  path('locations/', views.locations, name='location-list'),
  path('category/images/<int:category_name>', views.category_view, name='by_category'),
  path('location/images/<int:place>', views.location_view, name='by_location'),
  path('search-results/', views.search, name='image-search')
]