from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        "html_inline_text": "New Django Project"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contacts(request):
    return render(request, 'contacts.html')
