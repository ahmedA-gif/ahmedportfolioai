from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=100, default="AI Developer")
    role = models.CharField(max_length=100, default="Machine Learning Engineer")
    bio = models.TextField(default="Passionate AI developer building intelligent solutions")
    avatar = models.ImageField(upload_to='profile/', blank=True)
    location = models.CharField(max_length=100, default="Silicon Valley")
    website = models.URLField(blank=True)
    resume = models.FileField(upload_to='documents/', blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('ai_ml', 'AI/ML'),
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('tools', 'Tools'),
        ('cloud', 'Cloud'),
    ]
    
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0)
    icon = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['category', 'name']

class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
