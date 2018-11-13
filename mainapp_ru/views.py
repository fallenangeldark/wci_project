from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from mainapp_ru.models import HomeRu, InnerHomeRu
from mainapp_ru.forms import ClientAssesmentRu, EducationRu
from django.views import View
from django.db.models import Q

# Create your views here.

class Main_ru(TemplateView):
    model = HomeRu
    template_name = 'mainapp_ru/index.html'

    def get_context_data(self, **kwargs):
        context = super(Main_ru, self).get_context_data(**kwargs)
        context['home_ru'] = HomeRu.objects.get(name='education')
        context['title'] = 'Главная'
        return context

class Immigration_ru(Main_ru):
    template_name = 'mainapp_ru/immigration.html'

    def get_context_data(self, **kwargs):
        context = super(Main_ru, self).get_context_data(**kwargs)
        context['home_ru'] = HomeRu.objects.get(name='immigration')
        context['title'] = 'Иммиграция'
        return context

class Express_entry_ru(Immigration_ru):
    template_name = 'mainapp_ru/immigration_entry/express_entry.html'

    def get_context_data(self, **kwargs):
        context = super(Immigration_ru, self).get_context_data(**kwargs)
        context['in_home_ru'] = InnerHomeRu.objects.get(name='immigration-express_entry')
        context['title'] = 'Express entry'
        return context

class Business_class_ru(Immigration_ru):
    template_name = 'mainapp_ru/immigration_entry/business_class.html'

    def get_context_data(self, **kwargs):
        context = super(Immigration_ru, self).get_context_data(**kwargs)
        context['in_home_ru'] = InnerHomeRu.objects.get(name='immigration-business_class')
        context['title'] = 'Бизнес иммиграция'
        return context

class Family_sponsorship_ru(Immigration_ru):
    template_name = 'mainapp_ru/immigration_entry/family_sponsorship.html'

    def get_context_data(self, **kwargs):
        context = super(Immigration_ru, self).get_context_data(**kwargs)
        context['in_home_ru'] = InnerHomeRu.objects.get(name='immigration-family_sponsorship')
        context['title'] = 'Семейное спонсорство'
        return context

class Caips_ru(Immigration_ru):
    template_name = 'mainapp_ru/immigration_entry/caips.html'

    def get_context_data(self, **kwargs):
        context = super(Immigration_ru, self).get_context_data(**kwargs)
        context['in_home_ru'] = InnerHomeRu.objects.get(name='immigration-caips')
        context['title'] = 'Записи CAIPS'
        return context

class Custodianship_ru(Immigration_ru):
    template_name = 'mainapp_ru/immigration_entry/custodianship.html'

    def get_context_data(self, **kwargs):
        context = super(Immigration_ru, self).get_context_data(**kwargs)
        context['in_home_ru'] = InnerHomeRu.objects.get(name='immigration-custodianship')
        context['title'] = 'Опекунство'
        return context

class Visit_ru(Main_ru):
    template_name = 'mainapp_ru/visit.html'

    def get_context_data(self, **kwargs):
        context = super(Main_ru, self).get_context_data(**kwargs)
        context['home_ru'] = HomeRu.objects.get(name='visit')
        context['title'] = 'Посещение Канады'
        return context

class Life_ru(Main_ru):
    template_name = 'mainapp_ru/life.html'

    def get_context_data(self, **kwargs):
        context = super(Main_ru, self).get_context_data(**kwargs)
        context['home_ru'] = HomeRu.objects.get(name='life')
        context['title'] = 'Жизнь в Канаде'
        return context

class Arrival_ru(Life_ru):
    template_name = 'mainapp_ru/life_entry/arrival.html'

    def get_context_data(self, **kwargs):
        context = super(Life_ru, self).get_context_data(**kwargs)
        context['in_home_ru'] = InnerHomeRu.objects.get(name='life-arrival')
        context['title'] = 'Прибытие в Канаду'
        return context

class Health_ins_ru(Life_ru):
    template_name = 'mainapp_ru/life_entry/health_ins.html'

    def get_context_data(self, **kwargs):
        context = super(Life_ru, self).get_context_data(**kwargs)
        context['in_home_ru'] = InnerHomeRu.objects.get(name='life-health_ins')
        context['title'] = 'Страхование здоровья'
        return context

class Pl_to_live_ru(Life_ru):
    template_name = 'mainapp_ru/life_entry/pl_to_live.html'

    def get_context_data(self, **kwargs):
        context = super(Life_ru, self).get_context_data(**kwargs)
        context['in_home_ru'] = InnerHomeRu.objects.get(name='life-pl_to_live')
        context['title'] = 'Жильё'
        return context

class Work_ru(Life_ru):
    template_name = 'mainapp_ru/life_entry/work.html'

    def get_context_data(self, **kwargs):
        context = super(Life_ru, self).get_context_data(**kwargs)
        context['in_home_ru'] = InnerHomeRu.objects.get(name='life-work')
        context['title'] = 'Работа в Канаде'
        return context

class Links_ru(Life_ru):
    template_name = 'mainapp_ru/life_entry/links.html'

    def get_context_data(self, **kwargs):
        context = super(Life_ru, self).get_context_data(**kwargs)
        context['in_home_ru'] = InnerHomeRu.objects.get(name='life-links')
        context['title'] = 'Полезные ресурсы'
        return context

class About_ru(Main_ru):
    template_name = 'mainapp_ru/about.html'

    def get_context_data(self, **kwargs):
        context = super(Main_ru, self).get_context_data(**kwargs)
        context['home_ru'] = HomeRu.objects.get(name='about')
        context['title'] = 'О проекте'
        return context

class Forms_ru(Main_ru):
    template_name = 'mainapp_ru/form_base.html'

    def get_context_data(self, **kwargs):
        context = super(Main_ru, self).get_context_data(**kwargs)
        context['home_ru'] = HomeRu.objects.get(name='forms')
        context['title'] = 'Формы'
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


class ClientAssesment_ru(View):
    template_name = 'mainapp_ru/client_assesment_form.html'

    form_class = ClientAssesmentRu
    initial = {
        #'form_en': ClientAssesment.objects.all(),
        'title': 'Form',

    }
    # tuple_input = (
    #     'id_name', 'id_travel_doc_name', 'id_email', 'id_address', 'id_contact_number', 'id_nationality', 'id_dob', 'id_off_lang_en', 'id_off_lang_fr','id_partner_lang'
    # )
    # tuple_area = (
    #     'id_school_progr_name', 'id_work_exp_canada', 'id_work_exp_home', 'id_partner_work_exp', 'id_memo'
    # )
    # tuple_radio = (
    # 'id_canadian_dipl', 'id_canadian_cert', 'id_valid_job', 'id_nomin_cert', 'partner_status_of_canada', 'id_partner_track', 'id_sibling_in_canada'
    # )
    # t_else = ('id_edu_level', 'id_partner_edu', 'id_marital_status','id_immigration_status')
    # tuple_marital = ('id_marital_status')
    # tuple_immigration = ('id_immigration_status')

    # def get_foo_display(self):
    #     return dict(ClientAssesment.CHOICE_EDU_LEVEL)[self.foo]

    def post(self, request, *args, **kwargs):
        formset = self.form_class(request.POST)
        if formset.is_valid():
            formset.save()
            print('THIS IS SAVE')
            return HttpResponseRedirect('/ru/education')
        else :
            print('THIS IS NOT SAVE')
            return render(request, self.template_name, {'formset': formset, 'title': 'Form'})

    def get(self, request, *args, **kwargs):
        formset = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'formset': formset, 'title': 'Form'
        })

class Education_ru(View):
    template_name = 'mainapp_ru/education_form.html'

    form_class = EducationRu
    initial = {
        #'form_en': ClientAssesment.objects.all(),
        'title': 'Форма "Образование"',
    }

    def post(self, request, *args, **kwargs):
        formset = self.form_class(request.POST)
        if formset.is_valid():
            formset.save()
            print('THIS IS SAVE')
            return HttpResponseRedirect('/ru/education')
        else :
            print('THIS IS NOT SAVE')
            return render(request, self.template_name, {'formset': formset, 'title': 'Форма "Образование"'})

    def get(self, request, *args, **kwargs):
        formset = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'formset': formset,'title': 'Форма "Образование"',
        })

def home_view(request):
    return redirect('/ru')

class SearchView(View):
    template_name = 'mainapp_ru/search.html'

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        list_class_items = ['h1', 'paragraph1','paragraph2','paragraph3','paragraph4','paragraph5','paragraph6','paragraph7','paragraph8','paragraph9','paragraph10','paragraph11','paragraph12','paragraph13']

        founded_articles = HomeRu.objects.filter(Q(h1__icontains=query)|Q(paragraph1__icontains=query)|Q(paragraph2__icontains=query)|Q(paragraph3__icontains=query)|Q(paragraph4__icontains=query)|Q(paragraph5__icontains=query)|Q(paragraph6__icontains=query)|Q(paragraph7__icontains=query)|Q(paragraph8__icontains=query)|Q(paragraph9__icontains=query)|Q(paragraph10__icontains=query)|Q(paragraph11__icontains=query)|Q(paragraph12__icontains=query)|Q(paragraph13__icontains=query))
        founded_inner_articles =  InnerHomeRu.objects.filter(Q(h1__icontains=query)|Q(paragraph1__icontains=query)|Q(paragraph2__icontains=query)|Q(paragraph3__icontains=query)|Q(paragraph4__icontains=query)|Q(paragraph5__icontains=query)|Q(paragraph6__icontains=query)|Q(paragraph7__icontains=query)|Q(paragraph8__icontains=query)|Q(paragraph9__icontains=query)|Q(paragraph10__icontains=query)|Q(paragraph11__icontains=query)|Q(paragraph12__icontains=query)|Q(paragraph13__icontains=query))
        links_founded_articles = []
        for link in founded_articles:
            links_founded_articles.append(link.link)
        links_founded_inner_articles = []
        for link in founded_inner_articles:
            links_founded_inner_articles.append(link.link)
        count = len(founded_articles) + len(founded_inner_articles)
        context = {
        'founded_articles': founded_articles,
        'founded_inner_articles': founded_inner_articles,
        'head_links': links_founded_articles,
        'inner_links': links_founded_inner_articles,
        'count': count,
        'title': 'Поиск',
        'query': query
        }
        return render(self.request, self.template_name, context)
