from django.shortcuts import render
from django.http import HttpResponse

# Homepage view function 
def index(request):
  homepage = {}
  return render (request, 'all-photos/index.html', homepage)