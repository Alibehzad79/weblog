from django.urls import path
from search_app.views import SearchArticleListView
app_name="search"
urlpatterns = [
    path('', SearchArticleListView.as_view(), name="search"),
]
