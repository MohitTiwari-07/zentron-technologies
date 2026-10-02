from django.contrib.sitemaps.views import sitemap
from django.urls import path
from . import views
from .sitemaps import StaticViewSitemap, ServiceSitemap

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('services/<slug:slug>/',views.service_detail,name='service_detail'),
    path('packages/',views.packages,name='packages'),
    path('industries/',views.industries,name='industries'),
    path('contact/',views.contact,name='contact'),
    path('thank-you/',views.thank_you,name='thank_you'),
    path('robots.txt',views.robots,name='robots'),
    path('sitemap.xml',sitemap,{'sitemaps':{'static':StaticViewSitemap,'services':ServiceSitemap}},name='sitemap'),
    path("portfolio/", views.portfolio, name="portfolio"),
path("portfolio/<slug:slug>/", views.portfolio_detail, name="portfolio_detail"),
]
