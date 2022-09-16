from email.policy import HTTP
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("Worked")
    return render(request, 'onlineStoreApp/index.html')