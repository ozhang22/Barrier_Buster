"""
WSGI config for Rick_Hansen_Barrier_Buster project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Rick_Hansen_Barrier_Buster.settings")

application = get_wsgi_application()
