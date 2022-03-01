from unicodedata import category
from django.shortcuts import render
from .models import Location, Image, Category

# Homepage view function 
def index(request):
    all_images = Image.objects.all()
    all_locations = Location.objects.all()
    all_categories = Category.objects.all()
    homepage ={"all_images": all_images, 'all_locations':all_locations, 'all_categories':all_categories}
    return render(request, 'all-photos/index.html', homepage)

def locationImg_results(request,location):
    images = Image.filter_by_location(location)
    all_locations = Location.objects.all()
    all_categories = Category.objects.all()
    location = {'images':images,'all_locations':all_locations, 'all_categories':all_categories }
   

    return render(request, 'all-photos/location.html',location)

# def nav_items(request):
#     all_locations = Location.objects.all()
#     locations = {'all_locations':all_locations}
#     return render(request, '/navbar.html', locations)
def search_results(request):
    if 'searchImg' in request.GET and request.GET['searchImg']:
        category = request.GET.get('searchImg')
        searched_images =Image.search_by_category(category)
        all_locations = Location.objects.all()
        all_categories = Category.objects.all()
        message = f'{category}'
        category_images = {'all_locations':all_locations, 'all_categories':all_categories, 'images':searched_images, 'message': message}
        return render(request, 'all-photos/search.html', category_images)
    else:
        message = 'Please type category to search'
        return render(request, 'all-photos/search.html', {'message':message})