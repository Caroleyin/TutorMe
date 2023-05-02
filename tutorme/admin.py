from django.contrib import admin
from .models import AppUser, Course, Review

class ReviewInLine(admin.StackedInline):
    model = Review
    extra = 0

class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title_text','review_text']}),
    ]
    list_display = ['title_text','review_text', 'user']
    search_fields = ['tite_text','review_text']

class AppUserAdmin(admin.ModelAdmin):
    inlines = [ReviewInLine]


admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Course)
admin.site.register(Review, ReviewAdmin)