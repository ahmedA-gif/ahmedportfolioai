from .models import Profile, SocialLink
from apps.projects.models import Category
from django.conf import settings

def global_context(request):
    """Add global context data available in all templates"""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    return {
        'site_profile': profile,
        'social_links': SocialLink.objects.filter(is_active=True),
        'project_categories': Category.objects.all(),
        'DEBUG': settings.DEBUG,
        'current_year': 2025,
    }
