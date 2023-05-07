from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.generic import ListView
from blog_app.models import ArticleModel
from blog_app.forms import ArticleCommentForm
from comment_app.models import Comment
from datetime import datetime
from seo_app.models import ArticlesSEO
from category_app.models import CategoryModel
from tag_app.models import TagModel
from category_app.models import CategoryModel
from seo_app.models import ArticleListSeo
from ads_app.models import ArticlePageAds
# Create your views here.


class ArticleListView(ListView):
    model = ArticleModel
    template_name = "blog/articles_list.html"
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(status=ArticleModel.Status.published).all().distinct().order_by('-date_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seo'] = ArticleListSeo.objects.last()
        return context


def article_detail(request, *args, **kwargs):
    template_name = 'blog/article_detail.html'
    pk = kwargs['pk']
    try:
        article = ArticleModel.objects.get(id=pk)
    except:
        raise Http404()

    if request.method == 'POST':
        form = ArticleCommentForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            website = form.cleaned_data.get('website')
            comment = form.cleaned_data.get('comment')
            new_comment = Comment.objects.create(article=article, name=name, email=email, website=website,
                                                 comment=comment, date_sent=datetime.now(), status=Comment.Status.unread)
            if new_comment is not None:
                new_comment.save()
                # TODO sent email for article author
                return redirect(article.get_absolute_url())
    else:
        form = ArticleCommentForm()
    try:
        article_seo = ArticlesSEO.objects.filter(article=article).last()
    except:
        article_seo = None
    related_articles = ArticleModel.objects.filter(
        category__slug__exact=article.category.slug).all().distinct()[:4]
    article.reach_count += 1  # TODO config with user IP
    article.impression_count += 1
    article.save()
    try:
        ads = ArticlePageAds.objects.filter(article=article, active=True).last()
    except:
        ads = False   
    context = {
        'article': article,
        'form': form,
        'related_articles': related_articles,
        'article_seo': article_seo,
        'ads': ads,
    }
    return render(request, template_name, context)


class CategoryModelListView(ListView):
    model = ArticleModel
    template_name = "blog/articles_list.html"
    context_object_name = 'page_obj'
    paginate_by = 10

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        return super().get_queryset().filter(status=ArticleModel.Status.published, category__slug=category_slug).all().distinct().order_by('-date_created')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_name"] = self.kwargs['category_slug']
        context["category"] = CategoryModel.objects.filter(slug=self.kwargs['category_slug'])
        return context
    

class TagModelListView(ListView):
    model = ArticleModel
    template_name = "blog/articles_list.html"
    context_object_name = 'page_obj'
    paginate_by = 10

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        return super().get_queryset().filter(status=ArticleModel.Status.published, tags__slug=tag_slug).all().distinct().order_by('-date_created')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_name"] = self.kwargs['tag_slug']
        context["tag"] = CategoryModel.objects.filter(slug=self.kwargs['tag_slug'])
        return context

def send_emails(emails, subject, text):
    return(emails, subject, text)

def sidebar(request):
    template_name = 'blog/sidebar.html'
    categories = CategoryModel.objects.all()
    tags = TagModel.objects.all()
    recent_posts = ArticleModel.objects.filter(status=ArticleModel.Status.published).order_by('-date_updated').all()[:4]
    context = {
        'categories': categories,
        'tags': tags,
        'recent_posts': recent_posts,
    }
    
    return render(request, template_name, context)

