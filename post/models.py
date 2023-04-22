from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


User = get_user_model()

class BlogPost(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="publier")
    content = models.TextField(blank=True, verbose_name="contenu")
    thumbnail = models.ImageField(blank=True, null=True, upload_to="blog")

    class Meta:
        ordering = ['-created_on']
        verbose_name = "article"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def author_or_default(self):
        if self.author:
            return self.author.username
        return "l'auteur inconnue"

    def get_absolute_url(self):
        return reverse("post:home")





