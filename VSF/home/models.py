from django.db import models

# Create your models here.
class blog(models.Model):
    blog_title = models.CharField(max_length=300)
    blog_description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.blog_title

class incubation(models.Model):
    page_structure = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.date_created)

class launchpad(models.Model):
    page_structure = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.date_created)

class accelaration(models.Model):
    page_structure = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.date_created)


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
    brand_name = models.CharField(max_length=300,null=True)
    image = models.ImageField(upload_to="startups/")
    founder_name = models.CharField(max_length=300,null=True)
    sector = models.CharField(max_length=300,null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.brand_name


class Events(models.Model):
    image = models.ImageField(upload_to="events/")
    link = models.URLField(max_length=1000,null=True)

    def __str__(self):
        return self.image.name


class StartupSessions(models.Model):
    image = models.ImageField(upload_to="startupSession/")
    link = models.URLField(max_length=1000,null=True)

    def __str__(self):
        return self.image.name


class PressReleases(models.Model):
    image = models.ImageField(upload_to="pressRelease/")

    def __str__(self):
        return self.image.name