from unicodedata import name
from . import views
from django.urls import path

app_name = "mainapp"

urlpatterns = [
    path("", views.products, name="all"),
    path("<int:category_id>", views.category, name="category"),
    path("<int:category_id>/<int:page>",
         views.category, name="category_with_page"),
    path("<int:product_id>", views.product, name="product"),

]
