from django.contrib import admin
from .models import Content, MediaChannel, PublishSchedule

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ["title", "content_type", "author", "status", "views", "created_at"]
    list_filter = ["content_type", "status"]
    search_fields = ["title", "author", "category"]

@admin.register(MediaChannel)
class MediaChannelAdmin(admin.ModelAdmin):
    list_display = ["name", "platform", "subscribers", "status", "content_count", "created_at"]
    list_filter = ["platform", "status"]
    search_fields = ["name"]

@admin.register(PublishSchedule)
class PublishScheduleAdmin(admin.ModelAdmin):
    list_display = ["content_title", "channel_name", "scheduled_date", "status", "published_url", "created_at"]
    list_filter = ["status"]
    search_fields = ["content_title", "channel_name"]
