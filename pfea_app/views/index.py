import urllib.parse as urlparse

from django.shortcuts import render

import feedparser

def index(request):
    context = {}

    feed = feedparser.parse('https://www.reddit.com/r/nba/.rss')
    # Las tres mas recientes son las primeras tres en el arreglo
    last_three_entries = feed.entries[:3]

    context['news'] = []
    for entry in last_three_entries:
        entry_dict = {}

        # google_link = entry.link
        # parsed = urlparse.parse_qs(urlparse.urlparse(google_li4nk).query)
        # link = parsed['url'][0]

        entry_dict['title'] = entry.title
        entry_dict['link'] = entry.link
        context['news'].append(entry_dict)

    return render(request, 'home/index.html', context)
