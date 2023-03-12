from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='indexfile'),
    path('entertainment', views.entertainment, name='entertainment'),
    path('sports',views.sports, name='sports'),
    path('politics',views.politics, name='politics'),
    path('business',views.business, name='business'),
    path('technology', views.technology, name='technology'),
    path('international', views.international, name='international'),
    path('india', views.india, name='india'),
    path('miscellaneous', views.miscellaneous, name='miscellaneous'),
]