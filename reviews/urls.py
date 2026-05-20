from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    RegisterView,
    BookListCreateView,
    BookDetailView,
    ReviewListCreateView,
    ReviewDetailView,
    ChangePasswordView,
)

urlpatterns = [
    path('register/', RegisterView.as_view()),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('change-password/', ChangePasswordView.as_view()),

    path('books/', BookListCreateView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),

    path(
        'books/<int:book_id>/reviews/',
        ReviewListCreateView.as_view()
    ),

    path(
        'reviews/<int:pk>/',
        ReviewDetailView.as_view()
    ),
]