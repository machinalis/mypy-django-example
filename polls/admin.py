from typing import Any, Dict, List, Optional, Tuple

from django.contrib import admin  # type: ignore

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

Title = Optional[str]
Options = Dict[str, Any]
FieldSet = Tuple[Title, Options]
FieldSets = List[FieldSet]

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]  # type: FieldSets
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
