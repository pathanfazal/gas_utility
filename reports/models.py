from django.db import models

class Report(models.Model):
    REPORT_TYPES = [
        ('pdf', 'PDF'),
        ('xls', 'Excel'),
    ]

    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    report_type = models.CharField(max_length=50, choices=REPORT_TYPES, db_index=True)
    is_generated = models.BooleanField(default=False)  # Tracks report generation status
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
