from django.contrib import admin
from .models import QuizQuestions, Answer


class ChoiceInline(admin.TabularInline):
    # model = Answer
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = []

    # inlines = [ChoiceInline]


admin.site.register(QuizQuestions, QuestionAdmin)
