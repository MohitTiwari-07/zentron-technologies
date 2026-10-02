from django.core.management.base import BaseCommand
from core.models import Portfolio


class Command(BaseCommand):
    help = "Create demo portfolio projects"

    def handle(self, *args, **options):

        portfolios = [
            {
                "title": "Coffee Shop Website",
                "slug": "coffee-shop",
                "category": "Food & Beverage",
                "short_description": "Modern coffee shop website with menu, offers, location and online enquiry sections.",
                "demo_url": "/portfolio/coffee-shop/",
                "order": 1,
            },
            {
                "title": "Real Estate Website",
                "slug": "real-estate",
                "category": "Real Estate",
                "short_description": "Premium real estate website for property listings, enquiries and lead generation.",
                "demo_url": "/portfolio/real-estate/",
                "order": 2,
            },
            {
                "title": "Building Maintenance Website",
                "slug": "building-maintenance",
                "category": "Maintenance",
                "short_description": "Professional website for building maintenance, technical services and service enquiries.",
                "demo_url": "/portfolio/building-maintenance/",
                "order": 3,
            },
            {
                "title": "Exhibition & Events Website",
                "slug": "exhibition-events",
                "category": "Events",
                "short_description": "Creative event and exhibition website designed to showcase services, events and enquiries.",
                "demo_url": "/portfolio/exhibition-events/",
                "order": 4,
            },
            {
                "title": "Restaurant Website",
                "slug": "restaurant",
                "category": "Restaurant",
                "short_description": "Elegant restaurant website with menu, gallery, reviews, location and reservation sections.",
                "demo_url": "/portfolio/restaurant/",
                "order": 5,
            },
            {
                "title": "Salon Website",
                "slug": "salon",
                "category": "Beauty & Salon",
                "short_description": "Modern salon website showcasing services, pricing, gallery and appointment enquiries.",
                "demo_url": "/portfolio/salon/",
                "order": 6,
            },
            {
                "title": "Gym & Fitness Website",
                "slug": "gym",
                "category": "Fitness",
                "short_description": "High-energy fitness website with membership plans, trainers, programs and contact sections.",
                "demo_url": "/portfolio/gym/",
                "order": 7,
            },
            {
                "title": "Clinic Website",
                "slug": "clinic",
                "category": "Healthcare",
                "short_description": "Professional clinic website with doctors, treatments, services and appointment enquiry sections.",
                "demo_url": "/portfolio/clinic/",
                "order": 8,
            },
            {
                "title": "E-Commerce Website",
                "slug": "ecommerce",
                "category": "E-Commerce",
                "short_description": "Modern e-commerce storefront concept with products, categories, offers and shopping experience.",
                "demo_url": "/portfolio/ecommerce/",
                "order": 9,
            },
            {
                "title": "Construction Company Website",
                "slug": "construction",
                "category": "Construction",
                "short_description": "Corporate construction website featuring projects, services, capabilities and enquiry forms.",
                "demo_url": "/portfolio/construction/",
                "order": 10,
            },
            {
                "title": "Interior Design Website",
                "slug": "interior-design",
                "category": "Interior Design",
                "short_description": "Visual-first interior design website with projects, services, gallery and consultation enquiry.",
                "demo_url": "/portfolio/interior-design/",
                "order": 11,
            },
            {
                "title": "Automobile Website",
                "slug": "automobile",
                "category": "Automobile",
                "short_description": "Modern automobile website showcasing vehicles, services, features and customer enquiries.",
                "demo_url": "/portfolio/automobile/",
                "order": 12,
            },
        ]

        for item in portfolios:
            Portfolio.objects.update_or_create(
                slug=item["slug"],
                defaults=item,
            )

        self.stdout.write(
            self.style.SUCCESS(
                "12 portfolio projects created successfully."
            )
        )