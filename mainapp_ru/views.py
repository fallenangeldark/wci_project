from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from mainapp_ru.models import HomeRu, InnerHomeRu, ClientAssesment
from mainapp_ru.forms import ClientAssesmentRu
from django.views.generic.base import RedirectView
from django.views import View

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

class Immigration_pro_ru(Main_ru):
    template_name = 'mainapp_ru/immigration_pro.html'

    def get_context_data(self, **kwargs):
        context = super(Main_ru, self).get_context_data(**kwargs)
        context['home_ru'] = InnerHomeRu.objects.all()[3]
        context['title'] = 'Для Профессионалов'
        return context

class Immigration_business_ru(Main_ru):
    template_name = 'mainapp_ru/immigration_business.html'

    def get_context_data(self, **kwargs):
        context = super(Main_ru, self).get_context_data(**kwargs)
        context['home_ru'] = InnerHomeRu.objects.all()[0]
        context['title'] = 'Для бизнеса'
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


class ClientAssesment_ru(View):
    template_name = 'mainapp_ru/form.html'

    form_class = ClientAssesmentRu
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
            return HttpResponseRedirect('/ru/education')
        else :
            print('THIS IS NOT SAVE')
            return render(request, self.template_name, {'formset': formset, 'title': 'Form', 'tuple_input': self.tuple_input, 'tuple_area': self.tuple_area, 'tuple_radio': self.tuple_radio,
            't_else': self.t_else, 'title': 'Form'})

    def get(self, request, *args, **kwargs):
        formset = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'formset': formset, 'title': 'Form', 'tuple_input': self.tuple_input, 'tuple_area': self.tuple_area, 'tuple_radio': self.tuple_radio,
        't_else': self.t_else, 'title': 'Form',
        })

def home_view(request):
    return redirect('/ru')
