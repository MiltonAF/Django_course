from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('Hello world sdd')

def about(request):
    return HttpResponse('Abput')