from django.conf import settings
from django.db import models
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    INCOME = 'INCOME'
    EXPENSE = 'EXPENSE'
    TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)

    class Meta:
        unique_together = ('user', 'name', 'type')
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.type})"


class Transaction(TimeStampedModel):
    TYPE_CHOICES = [
        ("INCOME", "Income"),
        ("EXPENSE", "Expense"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default="EXPENSE"
    )
    date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-date', '-id']

    def __str__(self):
        return f"{self.date} - {self.category.name}: {self.amount}"