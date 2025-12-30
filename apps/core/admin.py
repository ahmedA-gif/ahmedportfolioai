from django.contrib import admin
from .models import Profile,Skill,SocialLink

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['full_name','role','location','created_date']
    fields=['full_name','role','bio','avatar','location','website','resume','github','Linkedin','twitter']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display=['name','category','percentage']
    list_filter=['category']
    ordering=['category','name']

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display=['name','url','is_active']
    list_filter=['is_active']