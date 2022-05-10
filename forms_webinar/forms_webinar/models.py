from django.db import models
from django.urls import reverse_lazy

class NameModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.pk})"

    def get_absolute_url(self):
        return reverse_lazy("name", kwargs={"pk": self.pk})
