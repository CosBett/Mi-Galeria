from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name ='homepage'),
    path('location/<location>/', views.locationImg_results, name= 'location'),
    path('category/<category>/', views.categoryImg_results, name= 'category'),

    path('search/', views.search_results, name = 'search_results'),

    ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)