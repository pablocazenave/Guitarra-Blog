from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    #this is a link to another model. 
    
    title = models.CharField(max_length=200)
    #this is how you define text with a limited number of characters.

    text = models.TextField()
    #this is for long text without a limit. Sounds ideal for blog post content, right?

    created_date = models.DateTimeField(default=timezone.now)
    #this is a date and time.
    
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        #is a function/method for publishing a post
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        #is a function/method that returns the title of our post
        return self.title