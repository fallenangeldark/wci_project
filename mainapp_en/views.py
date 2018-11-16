from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from mainapp_en.models import HomeEn, InnerHomeEn
from mainapp_en.forms import ClientAssesmentEn, EducationEn
from django.views import View
from django.db.models import Q
from django.shortcuts import render_to_response
# from django.views.generic.base import RedirectView
# from datetime import datetime
# from django.urls import reverse


# Create your views here.

class Main_en(TemplateView):
    model = HomeEn
    template_name = 'mainapp_en/index.html'

    def get_context_data(self, **kwargs):
        context = super(Main_en, self).get_context_data(**kwargs)
        context['home_en'] = HomeEn.objects.get(name='education_en')
        context['title'] = 'Main'
        return context

class Immigration_en(Main_en):
    template_name = 'mainapp_en/immigration.html'

    def get_context_data(self, **kwargs):
        context = super(Main_en, self).get_context_data(**kwargs)
        context['home_en'] = HomeEn.objects.get(name='immigration_en')
        context['title'] = 'Immigration'
        return context

class Express_entry_en(Immigration_en):
    template_name = 'mainapp_en/immigration_entry/express_entry.html'

    def get_context_data(self, **kwargs):
        context = super(Immigration_en, self).get_context_data(**kwargs)
        context['in_home_en'] = InnerHomeEn.objects.get(name='immigration-express_entry_en')
        context['title'] = 'Express entry'
        return context

class Business_class_en(Immigration_en):
    template_name = 'mainapp_en/immigration_entry/business_class.html'

    def get_context_data(self, **kwargs):
        context = super(Immigration_en, self).get_context_data(**kwargs)
        context['in_home_en'] = InnerHomeEn.objects.get(name='immigration-business_class_en')
        context['title'] = 'Business class'
        return context

class Family_sponsorship_en(Immigration_en):
    template_name = 'mainapp_en/immigration_entry/family_sponsorship.html'

    def get_context_data(self, **kwargs):
        context = super(Immigration_en, self).get_context_data(**kwargs)
        context['in_home_en'] = InnerHomeEn.objects.get(name='immigration-family_sponsorship_en')
        context['title'] = 'Family sponsorship'
        return context

class Caips_en(Immigration_en):
    template_name = 'mainapp_en/immigration_entry/caips.html'

    def get_context_data(self, **kwargs):
        context = super(Immigration_en, self).get_context_data(**kwargs)
        context['in_home_en'] = InnerHomeEn.objects.get(name='immigration-caips_en')
        context['title'] = 'CAIPS Notes'
        return context

class Custodianship_en(Immigration_en):
    template_name = 'mainapp_en/immigration_entry/custodianship.html'

    def get_context_data(self, **kwargs):
        context = super(Immigration_en, self).get_context_data(**kwargs)
        context['in_home_en'] = InnerHomeEn.objects.get(name='immigration-custodianship_en')
        context['title'] = 'Custodianship'
        return context

class Visit_en(Main_en):
    template_name = 'mainapp_en/visit.html'

    def get_context_data(self, **kwargs):
        context = super(Main_en, self).get_context_data(**kwargs)
        context['home_en'] = HomeEn.objects.get(name='visit_en')
        context['title'] = 'Visit to Canada'
        return context

class Life_en(Main_en):
    template_name = 'mainapp_en/life.html'

    def get_context_data(self, **kwargs):
        context = super(Main_en, self).get_context_data(**kwargs)
        context['home_en'] = HomeEn.objects.get(name='life_en')
        context['title'] = 'Life in Canada'
        return context

class Arrival_en(Life_en):
    template_name = 'mainapp_en/life_entry/arrival.html'

    def get_context_data(self, **kwargs):
        context = super(Life_en, self).get_context_data(**kwargs)
        context['in_home_en'] = InnerHomeEn.objects.get(name='life-arrival_en')
        context['title'] = 'Arrival to Canada'
        return context

class Health_ins_en(Life_en):
    template_name = 'mainapp_en/life_entry/health_ins.html'

    def get_context_data(self, **kwargs):
        context = super(Life_en, self).get_context_data(**kwargs)
        context['in_home_en'] = InnerHomeEn.objects.get(name='life-health_ins_en')
        context['title'] = 'Health Insurance'
        return context

class Pl_to_live_en(Life_en):
    template_name = 'mainapp_en/life_entry/pl_to_live.html'

    def get_context_data(self, **kwargs):
        context = super(Life_en, self).get_context_data(**kwargs)
        context['in_home_en'] = InnerHomeEn.objects.get(name='life-pl_to_live_en')
        context['title'] = 'Place to live'
        return context

class Work_en(Life_en):
    template_name = 'mainapp_en/life_entry/work.html'

    def get_context_data(self, **kwargs):
        context = super(Life_en, self).get_context_data(**kwargs)
        context['in_home_en'] = InnerHomeEn.objects.get(name='life-work_en')
        context['title'] = 'Work in Canada'
        return context

class Links_en(Life_en):
    template_name = 'mainapp_en/life_entry/links.html'

    def get_context_data(self, **kwargs):
        context = super(Life_en, self).get_context_data(**kwargs)
        context['in_home_en'] = InnerHomeEn.objects.get(name='life-links_en')
        context['title'] = 'Useful links'
        return context

class About_en(Main_en):
    template_name = 'mainapp_en/about.html'

    def get_context_data(self, **kwargs):
        context = super(Main_en, self).get_context_data(**kwargs)
        context['home_en'] = HomeEn.objects.get(name='about_en')
        context['title'] = 'About us'
        return context

class Forms_en(Main_en):
    template_name = 'mainapp_en/form_base.html'

    def get_context_data(self, **kwargs):
        context = super(Main_en, self).get_context_data(**kwargs)
        context['home_en'] = HomeEn.objects.get(name='forms_en')
        context['title'] = 'Forms'
        return context

class ClientAssesment_en(View):
    template_name = 'mainapp_en/client_assesment_form.html'

    form_class = ClientAssesmentEn
    initial = {
        #'form_en': ClientAssesment.objects.all(),
        'title': 'Form',

    }
    # tuple_input = (
    #     'id_travel_doc_name', 'id_email', 'id_address', 'id_contact_number', 'id_nationality', 'id_dob', 'id_off_lang_en', 'id_off_lang_fr','id_partner_lang'
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
            return HttpResponseRedirect('/en/redirect')
            # return render('mainapp_en/redirect.html')
        else :
            print('THIS IS NOT SAVE')
            return render(request, self.template_name, {'formset': formset, 'title': 'Assesment Form', 'title': 'Form'})

    def get(self, request, *args, **kwargs):
        formset = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'formset': formset, 'title': 'Assesment Form', 'title': 'Form',
        })
class Education_en(View):
    template_name = 'mainapp_en/education_form.html'

    form_class = EducationEn
    initial = {
        #'form_en': ClientAssesment.objects.all(),
        'title': 'Education form',
    }

    def post(self, request, *args, **kwargs):
        formset = self.form_class(request.POST)
        if formset.is_valid():
            formset.save()
            print('THIS IS SAVE')
            return HttpResponseRedirect('/en/redirect')
        else :
            print('THIS IS NOT SAVE')
            return render(request, self.template_name, {'formset': formset, 'title': 'Education Form'})

    def get(self, request, *args, **kwargs):
        formset = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'formset': formset,'title': 'Education Form',
        })

def home_view_en(request):
    return redirect('')

class SearchView(View):
    template_name = 'mainapp_en/search.html'

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        list_class_items = ['h1', 'paragraph1','paragraph2','paragraph3','paragraph4','paragraph5','paragraph6','paragraph7','paragraph8','paragraph9','paragraph10','paragraph11','paragraph12','paragraph13']

        founded_articles = HomeEn.objects.filter(Q(h1__icontains=query)|Q(paragraph1__icontains=query)|Q(paragraph2__icontains=query)|Q(paragraph3__icontains=query)|Q(paragraph4__icontains=query)|Q(paragraph5__icontains=query)|Q(paragraph6__icontains=query)|Q(paragraph7__icontains=query)|Q(paragraph8__icontains=query)|Q(paragraph9__icontains=query)|Q(paragraph10__icontains=query)|Q(paragraph11__icontains=query)|Q(paragraph12__icontains=query)|Q(paragraph13__icontains=query))
        founded_inner_articles =  InnerHomeEn.objects.filter(Q(h1__icontains=query)|Q(paragraph1__icontains=query)|Q(paragraph2__icontains=query)|Q(paragraph3__icontains=query)|Q(paragraph4__icontains=query)|Q(paragraph5__icontains=query)|Q(paragraph6__icontains=query)|Q(paragraph7__icontains=query)|Q(paragraph8__icontains=query)|Q(paragraph9__icontains=query)|Q(paragraph10__icontains=query)|Q(paragraph11__icontains=query)|Q(paragraph12__icontains=query)|Q(paragraph13__icontains=query))
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
        'title': 'Search',
        'query': query
        }
        return render(self.request, self.template_name, context)

def redirect_page(request):
    template_name = 'mainapp_en/redirect.html'
    return render(request, 'mainapp_en/redirect.html')

# Обработка ошибки 404

from django.template import RequestContext



def handler404(request, template_name="mainapp_en/404.html"):
    response = render_to_response("mainapp_en/404.html")
    response.status_code = 404
    return response
