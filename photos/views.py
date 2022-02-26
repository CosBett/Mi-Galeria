from django.shortcuts import render
from django.http import HttpResponse
from .models import Location, Image, Category

# Homepage view function 
def index(request):
  all_images = Image.objects.all()
  homepage ={"all_images": all_images}
  return render (request, 'all-photos/index.html', homepage)