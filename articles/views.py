from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from aquaticore.articles.models import Article
from django.contrib.comments.views.comments import post_free_comment
from django.http import HttpResponseRedirect
from django import forms
import datetime

def index(request):
    latest_article_list = Article.objects.all().order_by('-created')[:5]
    return render_to_response('articles/index.html', {'latest_article_list': latest_article_list})
    
def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render_to_response('articles/detail.html', {'article': article})

def article_post_free_comment(request):
	if request.has_key('url') and not request.has_key('preview'):
		response = post_free_comment(request)
		
		# Check there's a url to redirect to, and that post_free_comment worked
		if len(request['url'].strip()) > 0 and isinstance(response, HttpResponseRedirect):
			return HttpResponseRedirect(request['url'])
		
		# Fall back on the default post_free_comment response
		return response
	
	return post_free_comment(request)

class ArticleForm(forms.Form):
    title    = forms.CharField(max_length=150)
    body     = forms.CharField(widget=forms.Textarea)

def new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
			article = Article(title=request.REQUEST['title'], body=request.REQUEST['body'], created=datetime.datetime.now())
			article.save()			
			return HttpResponseRedirect('/articles/' + str(article.id))
    else:
        form = ArticleForm()
    return render_to_response('articles/new.html', {'form': form})

def delete(request, article_id):
	article = Article(id=article_id)
	article.delete()
	
	return HttpResponseRedirect('/articles/')
	