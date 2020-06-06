from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Answer(models.Model):
    """Model defnition for Answer."""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        """Unicode representation of Answer."""
        return f'{self.user}'