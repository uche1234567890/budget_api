from rest_framework import serializers
from .models import Category, Transaction


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # don't expose user, since it's auto-filled in perform_create
        fields = ["id", "name", "created_at"]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        # don't expose user, handled automatically
        fields = ["id", "amount", "type", "category", "created_at"]