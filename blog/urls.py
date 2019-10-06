from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.recipe_post_index, name="index"),
    path("recipes/<int:pk>/", views.recipe_post_detail, name="detail"),
    path("recipes/<category>/", views.recipe_category, name="category"),
]
