import urllib.parse as urlparse

from django.shortcuts import render

import feedparser

def index(request):
    context = {}

    feed = feedparser.parse('https://www.google.com/alerts/feeds/08631104230436444761/3823783356340969957')
    # Las tres mas recientes son las primeras tres en el arreglo
    last_three_entries = feed.entries[:3]

    context['news'] = []
    for entry in last_three_entries:
        entry_dict = {}

        google_link = entry.link
        parsed = urlparse.parse_qs(urlparse.urlparse(google_link).query)
        link = parsed['url'][0]

        entry_dict['title'] = entry.title
        entry_dict['link'] = link
        context['news'].append(entry_dict)

    return render(request, 'home/index.html', context)
