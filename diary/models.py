from django.contrib.auth.models import User

from django.db import models
from django import forms


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    public = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    image = models.ImageField(upload_to='article_attachments', null=True)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    profile_image = models.ImageField(upload_to='articles/', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class ArticleFileAttachment(models.Model):
    article = models.ForeignKey('Article', null=True, on_delete=models.SET_NULL)
    file = models.FileField(upload_to='article_attachments')


class ArticleImageAttachment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.SET_NULL, null=True)
    file = models.ImageField(upload_to='artice_images')


class TopicAuthors(models.Model):
    user = models.ForeignKey('UserProfile', related_name='topic_authors', on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey('Topic', related_name='topic_authors', on_delete=models.CASCADE)


class Topic(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    users = models.ManyToManyField('UserProfile',
                                   through='TopicAuthors',
                                   verbose_name='Участники')
    community_website = models.URLField()

    def __str__(self):
        return self.name


class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'public', 'image']


class ImageForm(forms.ModelForm):
    class Meta:
        model = ArticleImageAttachment
        fields = ['file']
