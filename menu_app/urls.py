from django.urls import path
from . import views

app_name = 'menu_app'

urlpatterns = [
    path('', views.home, name='home'),  # Пример URL
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
    path('page4/', views.page4, name='page4'),
]