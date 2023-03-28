from django.shortcuts import render


def index(request):
    template_html = 'index.html'
    return render(request, template_html)
