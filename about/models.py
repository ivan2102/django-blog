from django.db import models

class About(models.Model):
    heading = models.CharField(max_length=25)
    description = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading
    
    class Meta:
        verbose_name_plural = 'About'

class SocialLinks(models.Model):
    social_networking = models.CharField(max_length=25)
    social_links = models.URLField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.social_networking
    
    class Meta:
        verbose_name_plural = 'Social Link'
