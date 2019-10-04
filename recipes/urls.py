from django.urls import path

from . import views

app_name = "recipes"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:dish_name>/', views.dish_view, name="detail")
]