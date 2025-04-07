from django.db import models
from django.utils.text import slugify

# Create your models here.

class AboutPage(models.Model):
    title = models.CharField(max_length=255, default="About us")
    description = models.TextField(default="Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    background_image = models.ImageField(upload_to='images/', blank=True, null=True)
    overlay_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

class IntroPage(models.Model):
    title = models.CharField(max_length=255, default="Welcome to our Clinic")
    subtitle = models.CharField(max_length=255, default="This is Dr Pro")
    description = models.TextField(default="Integer aliquet congue libero...")
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Milestone(models.Model):
    title = models.CharField(max_length=255)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.title}: {self.value}"


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    # title = models.CharField(max_length=100)
    # description = models.TextField()  # ممكن نستخدم ده كـ bio
    image = models.ImageField(upload_to='team_images/', null=True, blank=True)
    # qualifications = models.TextField(blank=True, null=True)  # المؤهلات
    # working_hours = models.CharField(max_length=100, blank=True, null=True)  # ساعات العمل
    # location = models.CharField(max_length=200, blank=True, null=True)  # الموقع

    def __str__(self):
        return self.name

