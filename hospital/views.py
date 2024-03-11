from django.shortcuts import render

# Create your views here.
def About(request):
    return render(request, 'about.html')
def Index(request):
    return render(request, 'index.html')