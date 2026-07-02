from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):

    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    CATEGORY_CHOICES = [
        ('Hardware', 'Hardware'),
        ('Software', 'Software'),
        ('Network', 'Network'),
        ('Account', 'Account'),
        ('Email', 'Email'),
        ('Security', 'Security'),
        ('Other', 'Other'),
    ]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    subject = models.CharField(max_length=200)

    description = models.TextField()

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Open'
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Other'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject