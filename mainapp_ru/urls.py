from django.urls import path
from django.conf.urls import url
import mainapp_ru.views as mainapp_ru
from django.views.generic.base import RedirectView
# import mainapp_en.views as mainapp_en
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include


app_name = 'mainapp_ru'

urlpatterns =[
    path('', RedirectView.as_view(url='education/')),
    path('education/', mainapp_ru.Main_ru.as_view(), name='home'),
    path('immigration/', mainapp_ru.Immigration_ru.as_view(), name='immigration'),
    path('immigration/express_entry', mainapp_ru.Express_entry_ru.as_view(), name='immigration-express_entry_ru'),
    path('immigration/business_class', mainapp_ru.Business_class_ru.as_view(), name='immigration_bus_ru'),
    path('immigration/family_sponsorship', mainapp_ru.Family_sponsorship_ru.as_view(), name='immigration-family_sponsorship_ru'),
    path('immigration/CAIPS', mainapp_ru.Caips_ru.as_view(), name='immigration-caips_ru'),
    path('immigration/custodianship', mainapp_ru.Custodianship_ru.as_view(), name='immigration-custodianship_ru'),
    path('visit/', mainapp_ru.Visit_ru.as_view(), name='visit'),
    path('life/', mainapp_ru.Life_ru.as_view(), name='life'),
    path('life/arrival', mainapp_ru.Arrival_ru.as_view(), name='life-arrival_ru'),
    path('life/health_insurance', mainapp_ru.Health_ins_ru.as_view(), name='life-health_ins_ru'),
    path('life/place_to_live', mainapp_ru.Pl_to_live_ru.as_view(), name='life-pl_to_live_ru'),
    path('life/work', mainapp_ru.Work_ru.as_view(), name='life-work_ru'),
    path('life/links', mainapp_ru.Links_ru.as_view(), name='life-links_ru'),
    path('about/', mainapp_ru.About_ru.as_view(), name='about'),
    path('forms/', mainapp_ru.Forms_ru.as_view(), name='forms'),
    path('forms/cl_as_form', mainapp_ru.ClientAssesment_ru.as_view(), name='client_assesment_form'),
    path('forms/edu_form', mainapp_ru.Education_ru.as_view(), name='education_form'),
    path('search', mainapp_ru.SearchView.as_view(), name='search_view'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
