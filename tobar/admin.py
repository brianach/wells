from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
from django.forms import ModelForm, Textarea  # test
from map.models import Well


# class WellInline(admin.StackedInline):
#    model = Well


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):

    # inlines = [WellInline]
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {
        'slug': ('title',),
    }
    summernote_fields = ('content',)

    def save_model(self, request, obj, form, change):
        obj.cures = obj.well.cures
        obj.location = f"{obj.well.townland}, {obj.well.county}"
        super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
