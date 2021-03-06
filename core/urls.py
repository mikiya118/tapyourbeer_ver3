"""tapyourbeer_ver3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
import common.views
import home.views
import user.views
import beer.views
import brewery.views
import venue.views
import accounts.views
admin.autodiscover()

urlpatterns = [
    url(r'^main/', common.views.index, name='index'),
    path('', common.views.index, name='index'),
    path('signup/', accounts.views.signup_index, name='signup'),
    path('', include('accounts.urls')),
    path("api/like/<int:comment_id>/", common.views.like, name="like"),
    path("api/comment_wish/<int:item_id>/", common.views.comment_wish, name="comment_wish"),
    path("api/beer_wish/<int:item_id>/", common.views.beer_wish, name="beer_wish"),
    path("api/brewery_wish/<int:item_id>/", common.views.brewery_wish, name="brewery_wish"),
    path("api/venue_wish/<int:item_id>/", common.views.venue_wish, name="venue_wish"),
    path('home/', home.views.Home, name='Home'),
    path('home/world/', home.views.world, name='world'),
    path('user/', user.views.showUserGet, name='showUserGet'),
    path('user-beer/', user.views.userBeerDetailGet, name='userBeerDetailGet'),
    path('beer/', beer.views.beerDetailGet, name='beerDetailGet'),
    path('brewery/', brewery.views.breweryDetailGet, name='breweryDetailGet'),
    path('venue/', venue.views.venueDetailGet, name='venueDetailGet'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
