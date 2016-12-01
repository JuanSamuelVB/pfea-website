from django.shortcuts import render_to_response
from django.template import RequestContext

def handler404(request):
    response = render_to_response(
        'error/404.html', 
        {}
    )
    response.status_code = 404
    return response
