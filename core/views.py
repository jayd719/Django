"""-------------------------------------------------------
Django: Core Views.py
-------------------------------------------------------
Author:  JD
ID:      91786
Uses:    Django
Version:  1.0.8
__updated__ = Sat Jan 04 2025
-------------------------------------------------------
"""

from django.shortcuts import render, HttpResponse

app_name = "core"


# index view
def index_view(request):
    return render(request, "core/index.html")
