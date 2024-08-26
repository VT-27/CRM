from django.contrib import admin
from .models import Record

# Register your models here. Whenever a new class is created in models.py, we need to register the model or database in admin.py. Once we register here, it would be visisble in Django frontend while loggin as admin

admin.site.register(Record)

