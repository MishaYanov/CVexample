from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
"""
Post class- 
"""
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    link = models.CharField(max_length=256, blank=True, null=True)
    tags = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    updtae_time = models.DateTimeField(blank=True, null=True)
    short_description = models.CharField(blank=True, null=True, max_length=250)
    #liked = models.ManyToManyField(User, related_name='blog_post') also need to create function
    

    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def approve_comment(self):
        return self.comments.filter(approved_comment=True)
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk":self.pk})
    
    
    def __str__(self):
        return self.title
    
        """ comment class

        Returns:
            [type]: [description]
        """
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete = models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()

        
    def get_absolute_url(self):
        return reverse("blog:post_list" )
    
    
    def __str__(self):
        return self.text