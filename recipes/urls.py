from django.urls import path

from . import views

app_name = "recipes"
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:dish_name>/', views.dish_view, name="dish_view")
]