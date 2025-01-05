from django.shortcuts import render, HttpResponse


# index view
def index_view(request):
    return render(request, "base.html")
