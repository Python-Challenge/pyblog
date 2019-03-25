from django.contrib.sitemaps import Sitemap
from django.shortcuts import resolve_url
from posts.models import Post


class PostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()
        #return Entry.objects.filter(is_draft=False)

    def location(self, obj):
        return resolve_url('Post:detail', pk=obj.pk)

    def lastmod(self, obj):
        return obj.created_at


class StaticSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return ['Post:list']

    def location(self, obj):
        return resolve_url(obj)
