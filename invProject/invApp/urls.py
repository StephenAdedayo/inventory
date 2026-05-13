from django.urls import path
from .views import home_view, product_list_view, product_update_view, product_create_view, product_delete_view


urlpatterns = [
    path("", home_view, name="home"),
    path("create/", product_create_view, name="product_create"),
    path("list/", product_list_view, name="product_list"),
    path("update/<int:product_id>/", product_update_view, name="product_update"),
    path("delete/<int:product_id>/", product_delete_view, name="product_delete"),
]