from django.shortcuts import render, redirect
from django.views.generic import ListView
from blog_app.models import ArticleModel
from django.http import Http404
from search_app.models import Search
from datetime import datetime
# Create your views here.


class SearchArticleListView(ListView):
    template_name = 'search/search.html'
    model = ArticleModel
    context_object_name = 'articles'

    def get_queryset(self):
        query = self.request.GET.get('q')
        try:
            search_query = Search.objects.filter(query_name=query).all()
            search_query = Search.objects.get(query_name=query)
            search_query.search_count += 1
            search_query.date_updated = datetime.now()
            search_query.save()
        except:
            search_query = Search.objects.create(query_name=query, date_created=datetime.now(
                ), date_updated=datetime.now(), search_count=1)
        return ArticleModel.objects.get_search(query=query, status=ArticleModel.Status.published).order_by('-date_created')