from django.contrib import admin
from .models import Project,Category,Technology

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug','color']
    prepopulated_fields={'slug':('name',)}

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display=['name','icon','color']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['title','category','featured','is_ai_project','complexity_level','created_date']
    list_filter=['category','featured','is_ai_project','complexity_level','created_date']
    search_fields=['title','description']
    prepopulated_fields={'slug':('title',)}
    filter_horizontal=['technologies']
    fieldsets=(
      ('Basic Information',{
          'fields':('title','slug','short_description','description','image')
      }),
      ('Categorization',{
          'fields':('category','technologies','complexity_level','is_ai_project')
      }),
      ('Links',{
          'fields':('github_url','live_url','demo_url')
      }),
      ('Status',{
          'fields':('featured',)
      })  
    )