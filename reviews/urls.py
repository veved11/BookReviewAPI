from django.urls import path
from .views import (
    RegisterView,
    BookListView,
    ReviewListCreateView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('books/', BookListView.as_view()),
    path('reviews/', ReviewListCreateView.as_view()),

    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]