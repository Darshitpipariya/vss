from django.db import models

# Create your models here.
class blog(models.Model):
    blog_title = models.CharField(max_length=300)
    blog_description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.blog_title


class news(models.Model):
    news_title = models.CharField(max_length=300)
    news_description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.news_title


class contact_details(models.Model):
    person_name = models.CharField(max_length=300)
    person_email_id = models.EmailField()
    subject = models.CharField(max_length=300)
    Message = models.TextField()

    def __str__(self):
        return self.person_email_id


class OurStartUp(models.Model):
    image = models.ImageField(upload_to="startups/")

    def __str__(self):
        return self.image.name


class Events(models.Model):
    image = models.ImageField(upload_to="events/")

    def __str__(self):
        return self.image.name


class StartupSessions(models.Model):
    image = models.ImageField(upload_to="startupSession/")

    def __str__(self):
        return self.image.name


class PressReleases(models.Model):
    image = models.ImageField(upload_to="pressRelease/")

    def __str__(self):
        return self.image.name
