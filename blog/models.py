from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body=models.TextField(max_length=100)
    created=models.DateTimeField(auto_created='true')
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering=('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


