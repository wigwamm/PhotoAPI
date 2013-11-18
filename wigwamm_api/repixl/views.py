from django.shortcuts import render
from django import http


# Create your views here.
from .models import RepixlImage

def create(request):


    # if request.method != 'POST':

    #     # bad request
    #     return http.HttpResponse(status=302)
    
    url = request.REQUEST.get('url')
    email_address = request.REQUEST.get('email_address')

    img = RepixlImage.objects.create(url=url, email_address=email_address)
    img.status = 'pending task queue'
    img.save()
    img.upload_to_dropbox()

    # create a task with this object.

    return http.HttpResponse(1)