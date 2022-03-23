import os
import django
from django.conf import settings

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "fakejira1"))

def boot_django():
    settings.configure(
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        DATABASES={
            "default":{
                "ENGINE":"django.db.backends.sqlite3",
                "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
            }
        },
        INSTALLED_APPS=(
<<<<<<< HEAD
            "fakejira1",
=======
            "fakejira",
>>>>>>> f909855b1e98a4b76e048fb236680d75f969f2a3
        ),
        TIME_ZONE="UTC",
        USE_TZ=True,
    )
    django.setup()
