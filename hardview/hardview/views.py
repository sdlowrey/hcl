import sys
from django.template import loader, Context
from django.http import HttpResponseServerError

def custom500(request):
    t = loader.get_template('500.html')
    type, value, tb = sys.exc_info()
    return HttpResponseServerError(
        t.render(Context({'exception_value': value,})
    ))
