# Zentron Technologies — Final Django Website

Premium, responsive, motion-focused website for `zentron.ae` based on the Zentron Technologies company profile.

## Included
- Modern responsive homepage with motion graphics, parallax-style visuals, hover/tilt effects, reveal animations and marquee
- About, Services, Service Detail, Packages, Industries, Contact and Thank You pages
- Django admin for services, packages, industries, projects, site settings and enquiries
- Contact/quote form with database storage and optional email notification
- WhatsApp CTA and click-to-call/email links
- SEO metadata, canonical URLs, robots.txt and sitemap.xml
- Production-oriented Django security settings
- WhiteNoise static files + Gunicorn deployment setup
- Seed command for the profile-approved content

## Local setup
```bash
python -m venv venv
# Windows:
venv\\Scripts\\activate
# macOS/Linux:
# source venv/bin/activate

pip install -r requirements.txt
copy .env.example .env   # Windows
# cp .env.example .env   # macOS/Linux

python manage.py migrate
python manage.py seed_content
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Production
Set a strong `SECRET_KEY`, `DEBUG=False`, correct `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, `SITE_URL`, database and SMTP variables. Then:

```bash
python manage.py migrate
python manage.py seed_content
python manage.py collectstatic --noinput
gunicorn config.wsgi:application
```

## Content accuracy
The package page uses `AED 1,499` only for the Starter Presence package because that price appears in the supplied company profile. The other profile packages are marked `Custom` rather than inventing prices.
