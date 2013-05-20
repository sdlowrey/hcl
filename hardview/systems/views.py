# Create your views here.
from django.http import HttpResponse
def list_all(request):
    return HttpResponse("Hello world")
