from django.core.management.base import BaseCommand
from core.models import SiteSettings, Service, Package, Industry

class Command(BaseCommand):
    help='Seed Zentron website content from the company profile.'
    def handle(self,*args,**kwargs):
        SiteSettings.objects.update_or_create(pk=1,defaults={
            'company_name':'Zentron Technologies','tagline':'Dubai Licensed IT & Digital Solutions Company',
            'phone':'+971 52 512 2024','whatsapp':'971525122024','email':'info@zentron.ae','address':'Dubai, UAE',
            'opening_hours':'Available for business enquiries',
            'footer_text':'Helping businesses build a stronger online presence through websites, branding, marketing, and digital support.'})
        services=[
            ('Website Development','website-development','Modern, responsive and high-performing websites tailored to your business goals.','Modern websites built around your goals, audience, content and conversion journey.','⌁'),
            ('E-Commerce Solutions','e-commerce-solutions','Secure and scalable online stores to help you sell with confidence.','E-commerce experiences designed for product discovery, trust, checkout and growth.','◇'),
            ('Social Media Management','social-media-management','Strategic content and management to grow your brand and engagement.','Keep your brand active with planned content, profile management and consistent communication.','◎'),
            ('Google Ads & Meta Ads','google-meta-ads','Targeted advertising campaigns to reach the right audience and generate quality inquiries.','Campaign setup and lead-focused optimization for Google and Meta advertising.','◉'),
            ('Search Engine Optimization (SEO)','seo','Improve your search rankings and get found by more potential customers.','Practical SEO foundations that improve search visibility and help customers discover your business.','⌕'),
            ('Branding & Graphic Design','branding-graphic-design','Memorable brand identities and high-quality designs that make your business stand out.','Visual identity and creative assets that keep your brand clear and consistent.','✧'),
            ('Google Business Profile Setup','google-business-profile','Get discovered locally with a fully optimized Google Business Profile.','Improve local visibility and make it easier for nearby customers to find and contact you.','⌂'),
            ('IT Support & Digital Consultation','it-support-consultation','Reliable support and expert guidance to help you make the right digital decisions.','Practical digital guidance and support for businesses that need a dependable technology partner.','◌'),
        ]
        for i,(name,slug,short,desc,icon) in enumerate(services,1):
            Service.objects.update_or_create(slug=slug,defaults={'name':name,'short_description':short,'description':desc,'icon':icon,'is_featured':True,'sort_order':i})
        packages=[
            ('Starter Presence','starter-presence','Get your business online with a professional presence.','AED 1,499','1–3 page website\nMobile responsive design\nWhatsApp & contact form\nBasic SEO setup'),
            ('Business Growth','business-growth','A complete solution to establish and grow your brand.','Custom','Up to 6 pages\nGoogle Business setup\nBranding support\nOn-page SEO + 1 month support'),
            ('Digital Management','digital-management','Keep your brand active and engaging across platforms.','Custom','Social media management\nMonthly creatives\nProfile optimization\nReporting & support'),
            ('Performance Ads','performance-ads','Drive targeted traffic and generate quality leads.','Custom','Google & Meta Ads\nCampaign setup\nLead-focused optimization\nMonthly report'),
        ]
        for i,(name,slug,desc,price,features) in enumerate(packages,1):
            Package.objects.update_or_create(slug=slug,defaults={'name':name,'label':f'0{i}','description':desc,'price':price,'features':features,'featured':i==2,'sort_order':i})
        industries=[
            ('Trading Companies','trading-companies','Digital solutions for import, export and general trading businesses.','↗'),
            ('Technical & Maintenance Services','technical-maintenance','Websites and marketing for MEP, facility management and technical service providers.','⚙'),
            ('Restaurants & Cafés','restaurants-cafes','Attract more customers with a strong website and online presence.','✦'),
            ('Retail & E-Commerce','retail-ecommerce','Powerful e-commerce solutions to sell online and grow your brand.','◇'),
            ('Real Estate & Local Services','real-estate-local-services','Build trust and generate leads with modern digital platforms.','⌂'),
            ('Clinics, Salons & Professional Services','clinics-salons-professional','Enhance your online presence and reach more clients with targeted digital solutions.','◎'),
        ]
        for i,(name,slug,desc,icon) in enumerate(industries,1):
            Industry.objects.update_or_create(slug=slug,defaults={'name':name,'description':desc,'icon':icon,'sort_order':i})
        self.stdout.write(self.style.SUCCESS('Zentron content seeded successfully.'))
