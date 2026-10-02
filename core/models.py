from django.db import models

class SiteSettings(models.Model):
    company_name = models.CharField(max_length=120, default='Zentron Technologies')
    tagline = models.CharField(max_length=180, default='Dubai Licensed IT & Digital Solutions Company')
    phone = models.CharField(max_length=40, default='+971 52 512 2024')
    whatsapp = models.CharField(max_length=40, default='971525122024')
    email = models.EmailField(default='info@zentron.ae')
    address = models.CharField(max_length=220, default='Dubai, UAE')
    opening_hours = models.CharField(max_length=180, default='Available for business enquiries')
    footer_text = models.TextField(default='Helping businesses build a stronger online presence through websites, branding, marketing, and digital support.')
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Site Settings'; verbose_name_plural = 'Site Settings'
    def __str__(self): return self.company_name

class Service(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=240)
    description = models.TextField()
    icon = models.CharField(max_length=20, default='✦')
    is_featured = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    class Meta: ordering = ['sort_order','name']
    def __str__(self): return self.name

class Package(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    label = models.CharField(max_length=80, blank=True)
    price = models.CharField(max_length=80, default='Custom')
    billing = models.CharField(max_length=80, blank=True)
    description = models.CharField(max_length=240)
    features = models.TextField(help_text='One feature per line')
    featured = models.BooleanField(default=False)
    sort_order = models.PositiveIntegerField(default=0)
    class Meta: ordering = ['sort_order']
    def feature_list(self): return [x.strip() for x in self.features.splitlines() if x.strip()]
    def __str__(self): return self.name

class Industry(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=240)
    icon = models.CharField(max_length=20, default='◈')
    sort_order = models.PositiveIntegerField(default=0)
    class Meta: ordering = ['sort_order','name']
    def __str__(self): return self.name

class Project(models.Model):
    title = models.CharField(max_length=160)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    class Meta: ordering = ['sort_order','title']
    def __str__(self): return self.title

class QuoteRequest(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=40)
    email = models.EmailField()
    service = models.CharField(max_length=120, blank=True)
    message = models.TextField(blank=True)
    website = models.CharField(max_length=200, blank=True)  # honeypot
    created_at = models.DateTimeField(auto_now_add=True)
    is_contacted = models.BooleanField(default=False)
    class Meta: ordering = ['-created_at']
    def __str__(self): return f'{self.name} — {self.service or "General enquiry"}'


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=100)
    short_description = models.TextField()
    image = models.ImageField(upload_to="portfolio/", blank=True, null=True)
    demo_url = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]

    def __str__(self):
        return self.title