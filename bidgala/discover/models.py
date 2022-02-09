from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from django.utils.html import mark_safe

# Create your models here.
from django.db import models
from datetime import datetime
from accounts.models import UserInfo
import uuid 

# Create your models here.
def path_edit_article_img(instance, filename):
    return '/'.join(['article', str(instance.id), 'article' + filename])

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True)
    show = models.BooleanField(default=True)
    created_by = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.name)

class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title =  models.CharField(max_length=500, blank=True, unique=True)
    body =  models.TextField(max_length=100000, blank=True)
    css = models.TextField(blank=True)
    img = models.ImageField(upload_to=path_edit_article_img, blank=True)
    main_img_source = models.CharField(max_length=500, blank=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, null=True)
    writer_name = models.CharField(max_length=500, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(default='', max_length=500, blank=True, unique=True, editable=True)
    like_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)
    show = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=datetime.now)
    keywords = models.CharField(max_length=1000, blank=True)
    deck = models.CharField(max_length=1000, blank=True)
    social_media = models.CharField(max_length=1000, blank=True)


    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        self.body = self.body.replace('class="row"', 'class="row_"')
        self.css = self.css.replace('.row{', '.row_{')
        super().save(*args, **kwargs)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.CharField(max_length=50000, blank=True)
    user =  models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="discover_article_comment_user")
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now)
    parent =  models.TextField(null=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id) 

class ArticleImage(models.Model):
    base = models.CharField(default=settings.BASE_AWS_IMG_URL, max_length=200)
    img = models.ImageField(upload_to=path_edit_article_img, blank=True)
    created_date = models.DateTimeField(default=datetime.now)

    def main_image(self):
        temp = settings.BASE_AWS_IMG_URL + str(self.img)
        return mark_safe('<img src="%s"  style="width:150px; height:150px" alt="No Image to preview"/>' % (temp))
    
# class Like(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
#     user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.id)