import os
import sys

sys.path.insert(0, "/home/zentyepp/zentron_repo")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()