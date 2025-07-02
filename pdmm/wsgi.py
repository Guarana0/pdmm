import sys
import os

sys.path.append('/home/site/wwwroot')  # ajuste conforme seu deploy

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pdmm.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
