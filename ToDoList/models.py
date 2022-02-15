from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('OPEN', 'OPEN'),
    ('WORKING', 'WORKING'),
    ('DONE', 'DONE'),
    ('OVERDUE', 'OVERDUE')
)


class ListModel(models.Model):
    id = models.AutoField(primary_key=True)
    Timestamp = models.DateTimeField(auto_now_add=True, editable = False, help_text='Created at')
    Title = models.CharField(max_length=100, blank=False)
    Description = models.CharField(max_length=1000, blank=False)
    DueDate = models.DateField(null=True, blank=True)
    Status = models.CharField(
        max_length=7,
        choices=STATUS_CHOICES,
        default='OPEN',
        blank=False
    )
