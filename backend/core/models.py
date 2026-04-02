from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=50, choices=[("article", "Article"), ("video", "Video"), ("podcast", "Podcast"), ("infographic", "Infographic"), ("gallery", "Gallery")], default="article")
    author = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=50, choices=[("draft", "Draft"), ("review", "Review"), ("published", "Published"), ("archived", "Archived")], default="draft")
    views = models.IntegerField(default=0)
    published_date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class MediaChannel(models.Model):
    name = models.CharField(max_length=255)
    platform = models.CharField(max_length=50, choices=[("website", "Website"), ("youtube", "YouTube"), ("podcast", "Podcast"), ("newsletter", "Newsletter"), ("social", "Social")], default="website")
    subscribers = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("paused", "Paused")], default="active")
    content_count = models.IntegerField(default=0)
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class PublishSchedule(models.Model):
    content_title = models.CharField(max_length=255)
    channel_name = models.CharField(max_length=255, blank=True, default="")
    scheduled_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[("scheduled", "Scheduled"), ("published", "Published"), ("cancelled", "Cancelled"), ("failed", "Failed")], default="scheduled")
    published_url = models.URLField(blank=True, default="")
    notes = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content_title
