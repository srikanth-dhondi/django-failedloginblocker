from setuptools import setup

setup(\
    name = "django-failedloginblocker",
    version = "1.0.0",
    author = "Alex Kuhl",
    description = "Django app for locking users after failed attempts based on usernames",
    url = "https://github.com/alexkuhl/django-failedloginblocker",
    include_package_data = True,
    zip_safe = False
)
