from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    TransactionListCreateView, TransactionDetailView
)

urlpatterns = [
    path("categories/", CategoryListCreateView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path("transactions/", TransactionListCreateView.as_view(), name="transaction-list"),
    path("transactions/<int:pk>/", TransactionDetailView.as_view(), name="transaction-detail"),
]