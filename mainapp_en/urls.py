from django.urls import path
import mainapp_en.views as mainapp_en
from django.views.generic.base import RedirectView
# import mainapp_ru.views as mainapp_ru

app_name = 'mainapp_en'

urlpatterns =[
    path('', RedirectView.as_view(url='education/')),
    path('education/', mainapp_en.Main_en.as_view(), name='home'),
    path('immigration/', mainapp_en.Immigration_en.as_view(), name='immigration'),
    path('immigration/express_entry', mainapp_en.Express_entry_en.as_view(), name='immigration-express_entry'),
    path('immigration/business_class', mainapp_en.Business_class_en.as_view(), name='immigration-business_class'),
    path('immigration/family_sponsorship', mainapp_en.Family_sponsorship_en.as_view(), name='immigration-family_sponsorship'),
    path('immigration/CAIPS', mainapp_en.Caips_en.as_view(), name='immigration-caips'),
    path('immigration/custodianship', mainapp_en.Custodianship_en.as_view(), name='immigration-custodianship'),
    path('visit/', mainapp_en.Visit_en.as_view(), name='visit'),
    path('life/', mainapp_en.Life_en.as_view(), name='life'),
    path('life/arrival', mainapp_en.Arrival_en.as_view(), name='life-arrival_en'),
    path('life/health_insurance', mainapp_en.Health_ins_en.as_view(), name='life-health_ins_en'),
    path('life/place_to_live', mainapp_en.Pl_to_live_en.as_view(), name='life-pl_to_live_en'),
    path('life/work', mainapp_en.Work_en.as_view(), name='life-work_en'),
    path('life/links', mainapp_en.Links_en.as_view(), name='life-links_en'),
    path('about/', mainapp_en.About_en.as_view(), name='about'),
    path('forms/', mainapp_en.Forms_en.as_view(), name='forms'),
    path('forms/cl_as_form', mainapp_en.ClientAssesment_en.as_view(), name='client_assesment_form'),
    path('forms/edu_form', mainapp_en.Education_en.as_view(), name='education_form'),
]
