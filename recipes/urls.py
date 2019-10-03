from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:dish_id>/', views.dish_view, name="dish_view")
]