"""-------------------------------------------------------
Django: Core Urls.py
-------------------------------------------------------
Author:  JD
ID:      91786
Uses:    Django
Version:  1.0.8
__updated__ = Sat Jan 04 2025
-------------------------------------------------------
"""

from django.urls import path
from core import views


urlpatterns = [
    path("", views.index_view, name="home"),
]
