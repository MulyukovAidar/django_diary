from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

# Create your views here.
from diary.models import Article, PostForm, ImageForm, ArticleImageAttachment
from . import helper


def index(request):
    # trending = helper.get_trending()
    template = loader.get_template('index.html')
    context = {
        'trending': Article.objects.all(),
    }
    return HttpResponse(template.render(context, request))


@login_required
def post_article(request):
    if request.method == 'POST':
        article_form = PostForm(request.POST, request.FILES)
        a = article_form.data.get('image')
        b = request.POST.get('image')
        if article_form.is_valid():
            article_instance = article_form.save(commit=False)
            article_instance.author = request.user.userprofile
            # image_form = ImageForm(request.POST, request.FILES)
            # if image_form.is_valid():
            # image_form_instance = image_form.save(commit=False)
            # image_form_instance.article = article_instance
            # image_form_instance.save()
            article_instance.save()
        return redirect('/post')

    # a = Article.objects.create(author=request.user.author, title=title, body=body)
    # a.save()
    else:
        template = loader.get_template('form.html')
        context = {
            'user': request.user,
        }
        return HttpResponse(template.render(context, request))
# title = request.POST.get('title', '')
# body = request.POST.get('body', '')
# public = request.POST.get('title', False)
