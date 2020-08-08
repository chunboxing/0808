from django.shortcuts import render

def home(request):
    return render(request, 'myweb/home.html')

def about(request):
    return render(request, 'myweb/about.html')

def blog(request):
    return render(request, 'myweb/blog.html')

def examples(request):
    return render(request, 'myweb/examples.html')

def contact(request):
    return render(request, 'myweb/contact.html')
