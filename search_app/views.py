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
    paginate_by = 1

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None and query != '': 
            try:
                search_query_name = Search.objects.filter(query_name=query).last()
                search_query_name.search_count += 1
                search_query_name.date_updated = datetime.now()
                search_query_name.save()
            except:
                new_search_query = Search.objects.create(query_name=query, date_created=datetime.now(), date_updated=datetime.now(), search_count=1)
                new_search_query.save()
            return ArticleModel.objects.get_search(query=query, status=ArticleModel.Status.published).order_by('-date_created')
        else:
            return ArticleModel.objects.filter(status=ArticleModel.Status.published).order_by('-date_created').all()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["last_posts"] = latest_posts = ArticleModel.objects.order_by('-date_created').all()[:3]
        context['query'] = query = self.request.GET.get('q')
        return context
        