# Standard library imports
from django.db import models
from datetime import datetime
import uuid

# Related third party imports

# Local application/library specific imports
from accounts.models import UserInfo

# Create your models here.

def path_edit_channel_img(instance, filename):
    return '/'.join(['channels', str(instance.id), 'channel' + filename])


def path_edit_post_img(instance, filename):
    return '/'.join(['post', str(instance.id), 'post' + filename])

class Channel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True)
    img = models.ImageField(upload_to=path_edit_channel_img, blank=True)
    show = models.BooleanField(default=True)
    desc = models.CharField(max_length=150, blank=True)
    created_by = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.id)

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title =  models.CharField(max_length=500, blank=True)
    question =  models.CharField(max_length=10000, blank=True)
    img = models.ImageField(upload_to=path_edit_post_img, blank=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    channel_id = models.ForeignKey(Channel, on_delete=models.CASCADE)
    like_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)
    show = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.id)

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.CharField(max_length=50000, blank=True)
    user =  models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now)
    parent =  models.TextField(null=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id) 

class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)