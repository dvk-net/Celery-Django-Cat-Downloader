from django.http import HttpResponse

# Create your views here.
from . import tasks

def home(request):
    tasks.download_a_cat.delay()
    return HttpResponse('<h1>Гружу кота!!!!</h1>')