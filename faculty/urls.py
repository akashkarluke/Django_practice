from django.urls import path
from faculty import views


urlpatterns = [
    path('http/',views.HttpResponse1),
    path('json/',views.jsonResponse1),
    path('json1/',views.jsonResponse2),
]