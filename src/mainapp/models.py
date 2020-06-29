from django.db import models
from django.utils import timezone 

class OpenChan(models.Model):
    site_name = models.CharField(max_length=20, default="OpenChan", unique=True)
    site_desc = models.CharField(max_length = 50, default="The Open Source Chan Software")
    custom_cursor = models.ImageField(blank=True, null=True, upload_to='cursor/')
    
    def __str__(self):
        return("Site Settings")
    class Meta:
        verbose_name = 'Openchan Instance'
        verbose_name_plural = 'Openchan Instance'

class News(models.Model):
    news_subject = models.CharField(max_length=30)
    news_content = models.TextField()
    news_date = models.DateTimeField(auto_now_add=True, blank=True)
    show_alert = models.BooleanField(default=False)
    def __str__(self):
        return(self.news_subject)
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

class Board(models.Model):
    board_url = models.CharField(max_length=4, primary_key=True)
    board_description = models.CharField(max_length=30)
    post_counter = models.BigIntegerField(default = 0)
    custom_cursor = models.ImageField(blank=True, null=True, upload_to='cursor/')

    def __str__(self):
        return str("/" + self.board_url + "/ - " + self.board_description)
    pass


class Post(models.Model):
    post_name = models.CharField(max_length=30, default="Anonymous")
    post_subject = models.CharField(max_length=50, blank=True)
    post_content = models.TextField()
    post_image = models.ImageField(upload_to='images/' , blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True)
    parent_post = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    parent_board = models.ForeignKey("Board", null=True, blank=True, on_delete=models.CASCADE)
    local_id = models.BigIntegerField(default = 0)
    mod_warning = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        if self.post_subject:
            return str(self.parent_board.board_url + str(self.local_id) + self.post_subject)
        else: 
            return str("/" + self.parent_board.board_url + "/ #" + str(self.local_id) + " - " + self.post_content[:30] + "...")


