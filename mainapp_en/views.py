from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from mainapp_en.models import HomeEn, InnerHomeEn


# Create your views here.

class Main_en(TemplateView):
    model = HomeEn
    template_name = 'mainapp_en/index.html'

    def get_context_data(self, **kwargs):
        context = super(Main_en, self).get_context_data(**kwargs)
        context['home_en'] = HomeEn.objects.all()[0]
        context['title'] = 'Main'
        return context

class Immigration_en(Main_en):
    template_name = 'mainapp_en/immigration.html'

    def get_context_data(self, **kwargs):
        context = super(Main_en, self).get_context_data(**kwargs)
        context['home_en'] = HomeEn.objects.all()[1]
        context['title'] = 'Immigration'
        return context

class Visit_en(Main_en):
    template_name = 'mainapp_en/visit.html'

    def get_context_data(self, **kwargs):
        context = super(Main_en, self).get_context_data(**kwargs)
        context['home_en'] = HomeEn.objects.all()[2]
        context['title'] = 'Visit to Canada'
        return context

class Life_en(Main_en):
    template_name = 'mainapp_en/life.html'

    def get_context_data(self, **kwargs):
        context = super(Main_en, self).get_context_data(**kwargs)
        context['home_en'] = HomeEn.objects.all()[3]
        context['title'] = 'Life in Canada'
        return context

class About_en(Main_en):
    template_name = 'mainapp_en/about.html'

    def get_context_data(self, **kwargs):
        context = super(Main_en, self).get_context_data(**kwargs)
        context['home_en'] = HomeEn.objects.all()[4]
        context['title'] = 'About us'
        return context
