from django.contrib import admin
from .models import Industry, Package, Project, QuoteRequest, Service, SiteSettings,Portfolio

admin.site.register(Portfolio)

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin): list_display=('company_name','phone','email','address','updated_at')
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin): list_display=('name','is_featured','sort_order'); list_editable=('is_featured','sort_order'); prepopulated_fields={'slug':('name',)}
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin): list_display=('name','price','featured','sort_order'); list_editable=('price','featured','sort_order'); prepopulated_fields={'slug':('name',)}
@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin): list_display=('name','sort_order'); list_editable=('sort_order',); prepopulated_fields={'slug':('name',)}
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin): list_display=('title','category','is_featured','sort_order'); list_editable=('is_featured','sort_order')
@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin): list_display=('name','phone','email','service','created_at','is_contacted'); list_filter=('is_contacted','created_at'); readonly_fields=('created_at',)
