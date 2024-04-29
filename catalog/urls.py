from pprint import pprint

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("books", views.BookViewSet, "book")
router.register("authors", views.AuthorViewSet, "author")

review_router = routers.NestedDefaultRouter(router, "books", lookup='book')
review_router.register("reviews", views.ReviewViewSet, 'review')
review_router.register("images", views.BookImageViewSet, "book-images")

urlpatterns = router.urls + review_router.urls

