from django.contrib import admin
from .models import Quiz, QuizQuestion


class ChoiceInline(admin.TabularInline):
    model = QuizQuestion
    extra = 0
    readonly_fields = ('id',)


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = []
    inlines = [ChoiceInline]
    readonly_fields = ('id',)


admin.site.register(Quiz, QuestionAdmin)
