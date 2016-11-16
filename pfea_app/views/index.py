from django.shortcuts import render
from django.views.generic import TemplateView

import feedparser

def index(request):
    context = {}

    feed = feedparser.parse('https://www.google.com/alerts/feeds/08631104230436444761/3823783356340969957')
    # Las ultimas tres son las primeras tres en el arreglo
    last_three_entries = feed.entries[:3]

    context['news'] = []
    for entry in last_three_entries:
        entry_dict = {}
        entry_dict['title'] = entry.title
        entry_dict['link'] = entry.link
        context['news'].append(entry_dict)

    return render(request, 'home/index.html', context)
