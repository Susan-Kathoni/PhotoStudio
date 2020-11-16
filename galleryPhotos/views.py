from django.shortcuts import render
from django.http  import HttpResponse, Http404
import datetime as dt
from gallery.models import Image, Category, image_location
from django import forms

# Create your views here.
def home(request):
    return  render(request, 'base.html')

def about(request):
    return  render(request, 'about.html') 

def search_results(request):
    '''
    Method to search by image_location or category
    '''
    if 'result' in request.GET and request.GET["result"]:
        search_term = request.GET.get("result")
        searched_images = Image.search_by_category(search_term)
       
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message, "images":searched_images})
    elif 'result' in request.GET and request.GET["result"]:
        search_term = request.GET.get("result")
        searched_images = Image.search_by_location(search_term)
        message = f"{search_term}"    

        return render(request, 'search.html', {"message":message, "images":searched_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message}) 

def view_image(request,image_id):
    '''
    Method to get image by id
    '''
    try:
        image = Picture.objects.get(id =  image_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "upload.html", {"image":image})

def category(request, id):
    '''
    Method to search by category
    '''
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'image.html',{"message": message})

