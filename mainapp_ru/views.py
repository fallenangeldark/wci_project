from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from mainapp_ru.models import HomeRu


# Create your views here.

# class Main_ru(TemplateView):
#     model = HomeRu
#     template_name = 'mainapp_ru/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(Main_ru, self).get_context_data(**kwargs)
#         context={}
#         context['home_ru'] = HomeRu.objects.all()[0]
#         context['title'] = 'Главная'
#         return context
    # def get(self, request):
    #     context={}
    #     context['home_ru'] = HomeRu.objects.all()[0]
    #     context['title'] = 'Главная'
    #     context['home_url'] = self.template_name
    #     return  context

    # def get(self, request):
    #     forms = self.form_class(None)
    #     blogs = self.model
    #     context = {'forms': forms, "blogs":blogs}
    #     return render(request, self.template_name, context)

def home_view(request):
    return redirect('/ru')

def homeRu(request):
    context = {}
    context['home_ru'] = HomeRu.objects.all()[0]
    context['title'] = 'Главная'
    return render(request, 'mainapp_ru/index.html', context)
