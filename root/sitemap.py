from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blogs.models import Post

class StaticSiteMap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
                return [
            'root:home',
            'root:contact',
            'blogs:blog_home',

        ]
    def location(self,item):
        return reverse(item)


class DynamicSiteMap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return  Post.objects.filter(status=True)
    
    def location(self,obj):
        return '/blogs/post_details/%s' % obj.id
