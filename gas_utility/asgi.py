# gas_utility/asgi.py
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gas_utility.settings')

application = get_asgi_application()
