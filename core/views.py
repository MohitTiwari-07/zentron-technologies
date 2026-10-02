from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET
from .forms import QuoteRequestForm
from .models import Industry, Package, Project, Service, Portfolio

def home(request):
    return render(request, 'core/home.html', {
        'services': Service.objects.filter(is_featured=True)[:8],
        "portfolios": Portfolio.objects.filter(is_active=True),
        'packages': Package.objects.all()[:4],
        'industries': Industry.objects.all()[:6],
        'projects': Project.objects.filter(is_featured=True)[:3],
        'process_items': ['Discover','Design','Build','Launch','Grow'],
        'ticker_items': ['WEBSITES','BRANDING','SEO','SOCIAL MEDIA','GOOGLE & META ADS','IT SUPPORT'],
        'form': QuoteRequestForm(),
        'page_title': 'Zentron Technologies | Digital Growth Partner in Dubai',
        'meta_description': 'Zentron Technologies is a Dubai licensed IT and digital solutions company providing websites, e-commerce, SEO, social media, advertising, branding and IT support.',
    })

def about(request):
    return render(request,'core/about.html',{'page_title':'About Zentron Technologies | Dubai','meta_description':'Learn about Zentron Technologies and our practical digital solutions for businesses across the UAE.'})

def services(request):
    return render(request,'core/services.html',{'services':Service.objects.all(),'page_title':'IT & Digital Services in Dubai | Zentron','meta_description':'Explore website development, e-commerce, SEO, social media, paid advertising, branding, Google Business Profile and IT support.'})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request,'core/service_detail.html',{'service':service,'page_title':f'{service.name} | Zentron Technologies','meta_description':service.short_description})

def packages(request):
    return render(request,'core/packages.html',{'packages':Package.objects.all(),'page_title':'Digital Service Packages | Zentron Technologies','meta_description':'Explore Zentron Technologies service packages for UAE businesses.'})

def industries(request):
    return render(request,'core/industries.html',{'industries':Industry.objects.all(),'page_title':'Industries We Serve | Zentron Technologies','meta_description':'Tailored digital solutions for trading, technical services, restaurants, retail, real estate, clinics, salons and professional services.'})

def contact(request):
    form = QuoteRequestForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        lead = form.save()
        body = f'New website enquiry\n\nName: {lead.name}\nPhone: {lead.phone}\nEmail: {lead.email}\nService: {lead.service}\nMessage: {lead.message}'
        try:
            send_mail(f'New website enquiry — {lead.name}', body, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_TO_EMAIL], fail_silently=True)
        except Exception:
            pass
        return redirect('thank_you')
    return render(request,'core/contact.html',{'form':form,'page_title':'Contact Zentron Technologies | Dubai','meta_description':'Contact Zentron Technologies for website, marketing, SEO, branding, advertising and IT support enquiries.'})

def thank_you(request): return render(request,'core/thank_you.html',{'page_title':'Thank You | Zentron Technologies'})

@require_GET
def robots(request):
    return HttpResponse(f'User-agent: *\nAllow: /\nDisallow: /admin/\n\nSitemap: {settings.SITE_URL}/sitemap.xml\n',content_type='text/plain')

def error_404(request, exception): return render(request,'404.html',status=404)
def error_500(request): return render(request,'500.html',status=500)


def portfolio(request):
    portfolios = Portfolio.objects.filter(is_active=True)
    return render(request, "portfolio.html", {
        "portfolios": portfolios,
        "page_title": "Portfolio | Zentron Technologies",
        "meta_description": "Explore website design and digital solution projects created by Zentron Technologies for businesses in the UAE.",
    })


def portfolio_detail(request, slug):
    project = get_object_or_404(
        Portfolio,
        slug=slug,
        is_active=True
    )

    return render(request, "portfolio_detail.html", {
        "project": project,
        "page_title": f"{project.title} | Zentron Technologies",
        "meta_description": project.short_description,
    })