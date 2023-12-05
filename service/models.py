from django.db import models


class Services(models.Model):
    TYPE_CHOICES = [
        ('Transcription', 'Transcription'),
        ('Caption', 'Caption'),
    ]

    TEXT_FORMAT_CHOICES = [
        ('Clean Verbatim', 'Clean Verbatim'),
        ('Full Verbatim', 'Full Verbatim'),
    ]

    PLAN_CHOICES = [
        ('Standard', 'Standard'),
        ('Speedy', 'Speedy'),
        ('Expedite', 'Expedite'),
    ]

    CAPTION_METHOD_CHOICES = [
        ('Closed Caption', 'Closed Caption'),
        ('Burned in Caption', 'Burned in Caption'),
    ]

    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    uploading_file = models.FileField(upload_to='uploads/')
    storing_link = models.URLField()
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    text_format = models.CharField(max_length=20, choices=TEXT_FORMAT_CHOICES, blank=True, null=True)
    caption_method = models.CharField(max_length=20, choices=CAPTION_METHOD_CHOICES, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Set text_format or caption_method to None based on the type
        if self.type == 'Transcription':
            self.caption_method = None
        elif self.type == 'Caption':
            self.text_format = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Service {self.id}: {self.type} - {self.plan}"