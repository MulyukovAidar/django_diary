from django.contrib import admin
from diary.models import Article
from diary.models import UserProfile
from diary.models import Topic

# Register your models here.

admin.site.register(Topic)
admin.site.register(UserProfile)
admin.site.register(Article)