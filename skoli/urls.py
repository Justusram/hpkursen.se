from django.contrib import admin
from django.urls import path, include

from django.contrib.sitemaps.views import sitemap
from .sitemaps import ProvSitemap, QuizSitemap, LandingPageSitemap, ProfilePageSitemap, ÖvningsBankenSitemap

sitemaps = {
    'prov': ProvSitemap,
    'övningbank': ÖvningsBankenSitemap,
    'quiz': QuizSitemap,
    
    'home': LandingPageSitemap,
    'profile_page': ProfilePageSitemap,
    
    # ... other sitemap classes ...
}



    # ... other URL patterns ...



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('', include('user_app.urls')),
    # path('', include('övning_app.urls')),
    path('api/', include('api.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]



