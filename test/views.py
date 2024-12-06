from django.http import HttpResponse

def index(request):
    return HttpResponse("Backend for shrinkurlnow")