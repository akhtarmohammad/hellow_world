from django.http import HttpResponse
def homePageVeiw(request):
    return HttpResponse('hello world')