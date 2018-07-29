from django.shortcuts import render, get_object_or_404
from tutorials.models import TutorialSeries


# Create your views here.
def tutorial_series_details(request, slug):
    object = get_object_or_404(TutorialSeries,slug=slug)
    template="tutorials/tutorialseries_detail.html"
    context = {
        'object':object,
    }
    return render(request, template, context)
