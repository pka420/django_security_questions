import os
import django
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    INSTALLED_APPS=[
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'rest_framework',
		'django_security_questions',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'test.db'),
        }
    },
)

django.setup()

if __name__ == "__main__":
    from django.core.management import call_command
    call_command('makemigrations', 'django_security_questions')

