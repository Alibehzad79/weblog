from django.contrib import admin
from comment_app.models import Comment
# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_sent', 'status')
    list_editable = ('status',)
    list_filter = ('date_sent', 'status')
    search_fields = ('name', 'email', 'comment', 'website')