from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Service

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'
    def items(self): return ['home','about','services','packages','industries','contact']
    def location(self, item): return reverse(item)

class ServiceSitemap(Sitemap):
    changefreq = 'monthly'; priority = 0.7
    def items(self): return Service.objects.all()
    def location(self, obj): return reverse('service_detail', kwargs={'slug':obj.slug})
