from django.db import models


class Subject(models.Model):
    TYPE_CHOICES = [
        (0, "Umum"),
        (1, "Jurusan"),
        (2, "Ekstrakurikuler"),
    ]

    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    type = models.SmallIntegerField(
        choices=TYPE_CHOICES, default=0, blank=False, null=False
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
