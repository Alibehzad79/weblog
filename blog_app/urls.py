from django.urls import path
from blog_app.views import ArticleListView, article_detail, CategoryModelListView, TagModelListView

app_name='blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='articles_list'),
    path('<int:pk>/<slug:slug>/', article_detail, name='article_detail'),
    path('categories/<slug:category_slug>/', CategoryModelListView.as_view(), name='article_category'),
    path('tags/<slug:tag_slug>/', TagModelListView.as_view(), name="article_tag"),
]
