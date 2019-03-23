from django.contrib.sitemaps import Sitemap # sitemapアプリのインポート
from .models import * 
# 略式で書いています。python的には、必要なモデルを一つずつ列挙していくのが推奨されていると思いますが
# ここでは省略します。


class IndexSitemap(Sitemap):
    def items(self):
        return ['top']

    def location(self, obj):
        return '/'
