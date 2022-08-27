from django.contrib import admin

from pollsapp.views import register
from .models import Question,Answer


# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)
