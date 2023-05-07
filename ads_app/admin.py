from django.contrib import admin
from ads_app.models import ArticlePageAds, AboutPageAds, ContactPageAds, HomePageAds

# Register your models here.

@admin.register(ArticlePageAds)
class ArticlePageAdsAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'date_created', 'expiry_date', 'pay', 'active')
    list_editable = ('expiry_date', 'active')
    list_filter = ('active', 'expiry_date', 'date_created')
    search_fields = ('title', 'creator__username', 'creator__email', 'url')

@admin.register(AboutPageAds)
class AboutPageAdsAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'date_created', 'expiry_date', 'pay', 'active')
    list_editable = ('expiry_date', 'active')
    list_filter = ('active', 'expiry_date', 'date_created')
    search_fields = ('title', 'creator__username', 'creator__email', 'url')

@admin.register(ContactPageAds)
class ContactPageAdsAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'date_created', 'expiry_date', 'pay', 'active')
    list_editable = ('expiry_date', 'active')
    list_filter = ('active', 'expiry_date', 'date_created')
    search_fields = ('title', 'creator__username', 'creator__email', 'url')

@admin.register(HomePageAds)
class HomePageAdsAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'date_created', 'expiry_date', 'pay', 'active')
    list_editable = ('expiry_date', 'active')
    list_filter = ('active', 'expiry_date', 'date_created')
    search_fields = ('title', 'creator__username', 'creator__email', 'url')            