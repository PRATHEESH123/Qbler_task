from django.db import models

# Create your models here.


class Choice(models.Model):
    """Model defnition for Choice."""

    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        """Unicode representation of Choice."""
        return f'{self.question}'