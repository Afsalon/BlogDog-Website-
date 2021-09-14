from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    text=models.TextField(max_length=1000)
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def get_absolute_url(self):
        return reverse('home_page')



class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author=models.CharField(max_length=50)
    text=models.TextField(max_length=1000)
    created_date=models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('detail_page')

    def approve(self):
        self.approved_comment=True
        self.save()
