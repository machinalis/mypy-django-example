from django.contrib import admin  # type: ignore

from .models import Question

admin.site.register(Question)
