from django.shortcuts import render

def main(request):
    return render(request, 'main/date.html')
def articles(request):
    return render(request, 'main/articles.html')
def profile(request):
    return render(request, 'main/profile.html')
def map(request):
    return render(request, 'main/map.html')
