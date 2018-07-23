from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from mainapp_ru.models import HomeRu


# Create your views here.

class Main_ru(TemplateView):
    model = HomeRu
    template_name = 'mainapp_ru/base.html'

    def get_context_data(self, **kwargs):
        context = super(Main_ru, self).get_context_data(**kwargs)
        context['home_ru'] = HomeRu.objects.all()[0]
        context['title'] = 'Главная'
        return context

def home_view(request):
    return redirect('/ru')
