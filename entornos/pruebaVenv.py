import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nombre_proyecto.settings')

import django
django.setup()

from my_app.models import MiModel1, MiModel2

