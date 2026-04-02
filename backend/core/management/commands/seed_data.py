from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Content, MediaChannel, PublishSchedule
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusMedia with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusmedia.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Content.objects.count() == 0:
            for i in range(10):
                Content.objects.create(
                    title=f"Sample Content {i+1}",
                    content_type=random.choice(["article", "video", "podcast", "infographic", "gallery"]),
                    author=f"Sample {i+1}",
                    status=random.choice(["draft", "review", "published", "archived"]),
                    views=random.randint(1, 100),
                    published_date=date.today() - timedelta(days=random.randint(0, 90)),
                    category=f"Sample {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Content records created'))

        if MediaChannel.objects.count() == 0:
            for i in range(10):
                MediaChannel.objects.create(
                    name=f"Sample MediaChannel {i+1}",
                    platform=random.choice(["website", "youtube", "podcast", "newsletter", "social"]),
                    subscribers=random.randint(1, 100),
                    status=random.choice(["active", "paused"]),
                    content_count=random.randint(1, 100),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 MediaChannel records created'))

        if PublishSchedule.objects.count() == 0:
            for i in range(10):
                PublishSchedule.objects.create(
                    content_title=f"Sample PublishSchedule {i+1}",
                    channel_name=f"Sample PublishSchedule {i+1}",
                    scheduled_date=date.today() - timedelta(days=random.randint(0, 90)),
                    status=random.choice(["scheduled", "published", "cancelled", "failed"]),
                    published_url=f"https://example.com/{i+1}",
                    notes=f"Sample notes for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 PublishSchedule records created'))
