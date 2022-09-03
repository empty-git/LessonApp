from django.urls import path

from . import views

urlpatterns = [
    path('themes/', views.index, name='index'),
    path('themes/get_file/<int:theme_id>/', views.get_file, name='get_file'),
    path('themes/get_theme/<int:theme_id>/',views.get_theme, name='get_theme')
]