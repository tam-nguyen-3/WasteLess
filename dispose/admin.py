from django.contrib import admin

# Register your models here.
from .models import MenuItem, Dispose

admin.site.register(MenuItem)
admin.site.register(Dispose)