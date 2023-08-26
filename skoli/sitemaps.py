from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from base.models import Prov, Quiz, Question, Choise  # Import your models

class ProvSitemap(Sitemap):
    changefreq = "always"
    priority = 0.6

    def items(self):
        return Prov.objects.all()

    def location(self, obj):
        return reverse('provbanken-page')  # Replace with the actual URL name
    
class ÖvningsBankenSitemap(Sitemap):
    changefreq = "always"
    priority = 0.6

    def items(self):
        return Quiz.objects.all()

    def location(self, obj):
        return reverse('övningar-page')  # Replace with the actual URL name

class QuizSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Quiz.objects.all()

    def location(self, obj):
        prov_id = obj.prov_id
        prov_title = obj.prov.title
        return reverse('quiz-page', args=[prov_title, prov_id, obj.id])



class LandingPageSitemap(Sitemap):
    changefreq = "always"
    priority = 0.7

    def items(self):
        return ['home']

    def location(self, obj):
        if obj == 'home':
            return '/'  # Replace with your Landing Page URL name

class ProfilePageSitemap(Sitemap):
    changefreq = "always"
    priority = 0.3

    def items(self):
        return ['profile']

    def location(self, obj):
        if obj == 'profile':
            return '/min-profil' # Replace with your Profile Page URL name


