from django.conf.urls import patterns, include, url
import articles.views

urlpatterns = [
	url(r'^all/$', articles.views.articles, name= 'articles_all'),
	url(r'^get/(?P<article_id>\d+)/$', articles.views.article, name= 'article_detail'),
	url(r'^language/(?P<language>[a-z\-]+)/$', articles.views.language),
	url(r'^create/$', articles.views.create),
	url(r'^delete/(?P<id>\d+)/$', articles.views.delete, name= 'delete_article'),
	url(r'^search/$', articles.views.search_references),
]
