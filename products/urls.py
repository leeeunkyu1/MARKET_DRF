from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.ProductsListAPIView.as_view(), name="products_list"),
    path("<int:products_pk>/", views.ProductsDetailAPIView.as_view(), name="products_detail"),
    path("<int:comments_pk>/comments/",
        views.CommentListAPIView.as_view(), name="comment_list"),
    path(
    "comments/<int:comment_pk>/",
    views.CommentDetailAPIView.as_view(),
    name="comment_detail",
),
    ]