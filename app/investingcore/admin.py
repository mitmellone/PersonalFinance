from django.contrib import admin

# Register your models here.
from .models import Position, Transaction

admin.site.register(Position)
admin.site.register(Transaction)
