from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Sum
from django.contrib.auth.models import User
from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer , RegisterSerializer, LoginSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

class SummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # Totals
        income = Transaction.objects.filter(user=user, type="INCOME").aggregate(total=Sum("amount"))["total"] or 0
        expense = Transaction.objects.filter(user=user, type="EXPENSE").aggregate(total=Sum("amount"))["total"] or 0
        balance = income - expense

        # Category breakdown
        categories = Category.objects.filter(user=user)
        category_summary = []
        for category in categories:
            total = Transaction.objects.filter(user=user, category=category).aggregate(total=Sum("amount"))["total"] or 0
            category_summary.append({
                "category": category.name,
                "total": total
            })

        return Response({
            "income": income,
            "expense": expense,
            "balance": balance,
            "by_category": category_summary
        })

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({"refresh": str(refresh), "access": str(refresh.access_token)}, status=status.HTTP_200_OK)