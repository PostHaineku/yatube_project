from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()

class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name="name")
    slug = models.SlugField(unique=True, blank=True, null=True, default=None)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(Group, blank=True, null=True,
                              on_delete=models.SET_NULL, related_name='posting')
    # насколько критично оставлять одинаковые related_name для разных моделей?

    class Meta:
        ordering = ["-pub_date"]
