# from datetime import datetime
# from django.contrib.auth.models import User
# from .models import Article
# from django.db.models import F, Q
#
#
# def get_article_path(article):
#     user_id = article.author.user.id
#     return 'article/' + str(user_id)
#
#
# def like_article(id):
#     article = Article.objects.get(pk=id)
#     if article is not None:
#         article.rating = F('rating') + 1
#         article.save()
#
#
# def dislike_article(id):
#     article = Article.objects.get(pk=id)
#     if article is not None:
#         article.update(rating=F('rating') - 1)
#
#
# def get_trending():
#     return Article.objects.get(Q(created_at__day=datetime.now().day) |
#                                Q(created_at__month=datetime.now().month), Q(rating__gt=1))[:10]
#
#
# def create_users():
#     user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#     user.save()
#     user = User.objects.create_user('lalala', 'lennon@thebeatles.com', 'lalala')
#     user.save()