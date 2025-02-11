from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request, 'index.html',{'session_page':'home'})


def about_view(request):
    return render(request, 'about.html',{'session_page':'about'})

def courses_view(request):
    return render(request, 'courses.html' , {'session_page':'course'})

def team_view(request):
    return render(request, 'team.html', {'session_page':'pages'})

def contact_view(request):
    return render(request, 'contact.html', {'session_page':'contact'})

def testimonial_view(request):
    return render(request, 'testimonial.html', {'session_page':'pages'})

def error_view(request):
    return render(request, '404.html',{'session_page':'pages'})
