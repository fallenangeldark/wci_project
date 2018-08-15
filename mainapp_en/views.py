from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from mainapp_en.models import HomeEn, InnerHomeEn, ClientAssesment
from mainapp_en.forms import ClientAssesmentEn
from django.views import View
from django.views.generic.base import RedirectView
from datetime import datetime
from django.urls import reverse


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
        context['home_en'] = HomeEn.objects.all()[3]
        context['title'] = 'Immigration'
        return context

class Visit_en(Main_en):
    template_name = 'mainapp_en/visit.html'

    def get_context_data(self, **kwargs):
        context = super(Main_en, self).get_context_data(**kwargs)
        context['home_en'] = HomeEn.objects.all()[1]
        context['title'] = 'Visit to Canada'
        return context

class Life_en(Main_en):
    template_name = 'mainapp_en/life.html'

    def get_context_data(self, **kwargs):
        context = super(Main_en, self).get_context_data(**kwargs)
        context['home_en'] = HomeEn.objects.all()[2]
        context['title'] = 'Life in Canada'
        return context

class About_en(Main_en):
    template_name = 'mainapp_en/about.html'

    def get_context_data(self, **kwargs):
        context = super(Main_en, self).get_context_data(**kwargs)
        context['home_en'] = HomeEn.objects.all()[4]
        context['title'] = 'About us'
        return context

class ClientAssesment_en(View):
    template_name = 'mainapp_en/form.html'

    form_class = ClientAssesmentEn
    initial = {
        #'form_en': ClientAssesment.objects.all(),
        'title': 'Form',

    }
    tuple_input = (
        'id_name', 'id_travel_doc_name', 'id_email', 'id_address', 'id_contact_number', 'id_nationality', 'id_dob', 'id_off_lang_en', 'id_off_lang_fr','id_partner_lang'
    )
    tuple_area = (
        'id_school_progr_name', 'id_work_exp_canada', 'id_work_exp_home', 'id_partner_work_exp', 'id_memo'
    )
    tuple_radio = (
    'id_canadian_dipl', 'id_canadian_cert', 'id_valid_job', 'id_nomin_cert', 'partner_status_of_canada', 'id_partner_track', 'id_sibling_in_canada'
    )
    t_else = ('id_edu_level', 'id_partner_edu', 'id_marital_status','id_immigration_status')
    # tuple_marital = ('id_marital_status')
    # tuple_immigration = ('id_immigration_status')

    # def get_foo_display(self):
    #     return dict(ClientAssesment.CHOICE_EDU_LEVEL)[self.foo]

    def post(self, request, *args, **kwargs):
        formset = self.form_class(request.POST)
        if formset.is_valid():
            formset.save()
            print('THIS IS SAVE')
            return HttpResponseRedirect('/en/education')
        else :
            print('THIS IS NOT SAVE')
            return render(request, self.template_name, {'formset': formset, 'title': 'Form', 'tuple_input': self.tuple_input, 'tuple_area': self.tuple_area, 'tuple_radio': self.tuple_radio,
            't_else': self.t_else, 'title': 'Form'})

    def get(self, request, *args, **kwargs):
        formset = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'formset': formset, 'title': 'Form', 'tuple_input': self.tuple_input, 'tuple_area': self.tuple_area, 'tuple_radio': self.tuple_radio,
        't_else': self.t_else, 'title': 'Form',
        })

def home_view_en(request):
    return redirect('')
