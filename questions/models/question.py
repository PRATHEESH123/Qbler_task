from django.db import models

# Create your models here.


class Question(models.Model):
    """Model defnition for Question."""

    tittle = models.CharField(max_length=50)
    multiple = models.BooleanField()
    mandatory = models.BooleanField()

    def __str__(self):
        """Unicode representation of Question."""
        return f'{self.tittle}'