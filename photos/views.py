from django.shortcuts import render
from .models import Location, Image, Category

# Homepage view function 
def index(request):
    all_images = Image.objects.all()
    all_locations = Location.objects.all()

    homepage ={"all_images": all_images, 'all_locations':all_locations}
    return render(request, 'all-photos/index.html', homepage)

def img_location(request, location):
    images = Image.filter_by_location(location)
    location = {'images':images}
    return render(request, 'all-photos/location.html', location)
# def nav_items(request):
#     all_locations = Location.objects.all()
#     locations = {'all_locations':all_locations}
#     return render(request, '/navbar.html', locations)
def search_results(request):
    if 'searchImg' in request.GET and request.GET['searchImg']:
        search_term = request.GET.get('searchImg')
        searched_images =Image.search_image(search_term)
        message = f'{search_term}'
        displayed_images = {'images':searched_images, 'message': message}
        return render(request, ' all-photos/search.html', displayed_images)
    else:
        message = 'Please type term to search'
        return render(request, 'all-photos/search.html', {'message':message})