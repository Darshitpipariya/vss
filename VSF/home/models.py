from django.db import models
 
# Create your models here.
class blog(models.Model):
    blog_title = models.CharField(max_length=300)
    blog_description = models.TextField()
    date_created= models.DateTimeField(auto_now_add=True, null=True)
 
    def __str__(self):
        return self.blog_title
 
class news(models.Model):
    news_title = models.CharField(max_length=300)
    news_description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
 
    def __str__(self):
        return self.news_title