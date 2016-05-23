from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse
from articles.models import Article
from articles.forms import ArticleForm
from django.template import RequestContext

# Create your views here.

@login_required(login_url='/')
def articles(request):
	language = 'en-gb'
	session_language = 'en-gb'
	
	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']
		
	if 'lang' in request.session:
		session_language = request.session['lang']
	args = {}
	args.update(csrf(request))
	
	args['articles'] = Article.objects.all()
	args['language'] = language
	args['session_language'] = session_language
		
	return render_to_response('articles.html', args)
							
													 
@login_required(login_url='/')
def article(request, article_id=1):
	return render_to_response('article.html',
							{'article': Article.objects.get(id=article_id) })

@login_required(login_url='/')
def language(request, language='en-gb'):
	response = HttpResponse("setting language to %s" % language)
	
	response.set_cookie('lang', language)
	
	response.session['lang'] = language
	
	return response
	
@permission_required('articles.forms', raise_exception=True)
def create(request):
	if request.POST:
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			
			return HttpResponseRedirect('/data/all')
	else:
		form = ArticleForm()
		
	args = {}
	args.update(csrf(request))
	
	args['form'] = form
	
	return render_to_response('create_article.html', args)

@permission_required('articles.delete_article', raise_exception=True)
def delete(request, id):
   article_delete = Article.objects.get(pk = id)
   article_delete.delete()
   return HttpResponseRedirect('/data/all')
   
def search_references(request):
	if request.method == "POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''
			
	articles = Article.objects.filter(TAG_SNPs__contains = search_text)
	
	return render_to_response('ajax_search.html', {'articles' : articles})


