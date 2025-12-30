from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from apps.projects.models import Project
from apps.core.models import Skill, Profile, SocialLink
from .models import Contact, Service
from .forms import ContactForm

def home(request):
    """Home page with hero section and featured content"""
    profile = Profile.objects.first()
    featured_projects = Project.objects.filter(featured=True)[:3]
    ai_projects_count = Project.objects.filter(is_ai_project=True).count()
    skills = Skill.objects.all()[:8]  # Show top 8 skills
    services = Service.objects.filter(is_active=True)[:4]
    
    # AI-specific statistics
    stats = {
        'projects_completed': Project.objects.count(),
        'ai_models_trained': ai_projects_count,
        'years_experience': 1,
        'clients_satisfied': 10,
    }
    
    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'skills': skills,
        'services': services,
        'stats': stats,
        'page_title': 'AI Developer Portfolio - Building the Future with Intelligence'
    }
    return render(request, 'pages/home.html', context)

def about(request):
    """About page with detailed profile and skills"""
    profile = Profile.objects.first()
    skills_by_category = {}
    
    for skill in Skill.objects.all():
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)
    
    context = {
        'profile': profile,
        'skills_by_category': skills_by_category,
        'page_title': 'About - AI Developer & Machine Learning Expert'
    }
    return render(request, 'pages/about.html', context)

def contact(request):
    """Contact page with form handling"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # AJAX response
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Thank you! Your message has been sent. I\'ll get back to you soon!'
                })
            else:
                messages.success(request, 'Thank you! Your message has been sent successfully.')
                return redirect('contact')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                })
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'page_title': 'Contact - Let\'s Build AI Solutions Together'
    }
    return render(request, 'pages/contact.html', context)
