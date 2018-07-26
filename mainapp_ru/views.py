from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from mainapp_ru.models import HomeRu, InnerHomeRu


# Create your views here.

class Main_ru(TemplateView):
    model = HomeRu
    template_name = 'mainapp_ru/index.html'

    def get_context_data(self, **kwargs):
        context = super(Main_ru, self).get_context_data(**kwargs)
        context['home_ru'] = HomeRu.objects.all()[0]
        context['title'] = 'Главная'
        return context

class Immigration_ru(Main_ru):
    template_name = 'mainapp_ru/immigration.html'

    def get_context_data(self, **kwargs):
        context = super(Main_ru, self).get_context_data(**kwargs)
        context['home_ru'] = HomeRu.objects.all()[1]
        context['title'] = 'Иммиграция'
        return context

class Visit_ru(Main_ru):
    template_name = 'mainapp_ru/visit.html'

    def get_context_data(self, **kwargs):
        context = super(Main_ru, self).get_context_data(**kwargs)
        context['home_ru'] = HomeRu.objects.all()[2]
        context['title'] = 'Посещение Канады'
        return context

class Life_ru(Main_ru):
    template_name = 'mainapp_ru/life.html'

    def get_context_data(self, **kwargs):
        context = super(Main_ru, self).get_context_data(**kwargs)
        context['home_ru'] = HomeRu.objects.all()[3]
        context['title'] = 'Жизнь в Канаде'
        return context

class About_ru(Main_ru):
    template_name = 'mainapp_ru/about.html'

    def get_context_data(self, **kwargs):
        context = super(Main_ru, self).get_context_data(**kwargs)
        context['home_ru'] = HomeRu.objects.all()[4]
        context['title'] = 'О проекте'
        return context

# class Professionals_ru(InnerHomeRu):
#     model = InnerHomeRu
#     template_name = 'mainapp_ru/professionals.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(Professionals_ru, self).get_context_data(**kwargs)
#         context['outer_rel'] = InnerHomeRu.objects.filter(outer_relation__id=id)
#         context['home_ru'] = InnerHomeRu.objects.all()[0]
#         context['title'] = 'Для специалистов'
#         return context

def home_view(request):
    return redirect('/ru')
