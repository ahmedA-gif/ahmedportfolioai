from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    color = models.CharField(max_length=7, default="#00ffff")
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

class Technology(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=7, default="#ffffff")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ['name']

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='projects/', blank=True)
    technologies = models.ManyToManyField(Technology)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    is_ai_project = models.BooleanField(default=True)
    complexity_level = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ], default='intermediate')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-created_date']
