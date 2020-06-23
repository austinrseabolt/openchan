from django.db import models
from django.utils import timezone 


class Thread(models.Model):
    

    pass
    

class Post(models.Model):
    post_name = models.CharField(max_length=30, default="Anonymous")
    post_subject = models.CharField(max_length=50, blank=True)
    post_content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        if self.post_subject:
            return self.post_subject
        else: 
            return self.post_content[:50]


