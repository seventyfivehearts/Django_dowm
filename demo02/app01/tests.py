
from django.test import TestCase

# Create your tests here.
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo02.settings")
    import django
    django.setup()
    from app01 import models
    models.Book.objects.filter(pk__gt=1000).delete()