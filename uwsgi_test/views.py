from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s! changed!" % now

    return HttpResponse(html)
