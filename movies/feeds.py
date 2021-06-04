from django.contrib.syndication.views import Feed
from django.template.defaultfilters import title, truncatewords
from .models import Movie


class LastestPostsFeed(Feed):
    title = "my blog"
    link = ""
    description = "New posts of my blog"

    def items(self):
        return Movie.objects.all().order_by('id')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.title

    def item_link(self, item):
        return 'link'