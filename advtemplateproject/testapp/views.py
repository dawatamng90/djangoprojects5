from django.shortcuts import render

# Create your views here.
def base_view(request):
    return render(request,'testapp/base.html')

def movie_view(request):
    return render(request,'testapp/movie.html')

def sports_view(request):
    return render(request,'testapp/sports.html')

def politics_view(request):
    return render(request,'testapp/politics.html')