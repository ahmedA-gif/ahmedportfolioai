from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Project,Category,Technology

def project_list(request):
    projects=Project.objects.all()
    categories=Category.objects.all()
    technologies=Technology.objects.all()

    category_slug=request.GET.get('category')
    if category_slug:
        projects=projects.filter(category_slug=category_slug)
    
    tech_name=request.GET.get('technology')
    if tech_name:
        projects=projects.filter(technologies__name__icontains=tech_name)

    ai_only=request.GET.get('ai_only')
    if ai_only=="true":
        projects=projects.filter(is_ai_project=True)
    
    context={
        'projects':projects,
        'categories':categories,
        'technologies':technologies,
        'current_category':category_slug,
        'current_technology':tech_name,
        'ai_only':ai_only=='true',
        'page_title':'AI Projects - Innovative Machine Learning Solutions'
    }
    return render(request,'projects/project_list.html',context)

def project_detail(request,slug):
    project=get_object_or_404(Project,slug=slug)
    related_projects=Project.objects.filter(
        category=project.category
    ).exclude(id=project.id)[:3]
    context={
        'project':project,
        'related_projects':related_projects,
        'page_title':f"{project.title} - AI Project Details"
    }
    return render(request,'projects/project_detail.html',context)

def api_projects(request):
    category=request.GET.get('category','')
    ai_only=request.GET.get('ai_only','false')=='true'
    projects=Project.objects.all()

    if category:
        projects=projects.filter(category_slug=category)
    if ai_only:
        projects=projects.filter(is_ai_project=True)
    projects_data=[]
    for project in projects:
        projects_data.append({
            'id':project.id,
            'title':project.title,
            'description':project.short_description,
            'image':project.image.url if project.image else '',
            'technologies':[tech.name for tech in project.technologies.all() ],
            'category':{
                'name':project.category.name,
                'color':project.category.color
            },
            'github_url': project.github_url,
            'live_url': project.live_url,
            'demo_url': project.demo_url,
            'detail_url': project.get_absolute_url(),
            'is_ai_project': project.is_ai_project,
            'complexity_level': project.complexity_level,
        })
        return JsonResponse({'projects':projects_data})
          