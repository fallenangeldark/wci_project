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
    path('immigration/business', mainapp_ru.Immigration_business_ru.as_view(), name='immigration_bus'),
    path('immigration/for-professionals', mainapp_ru.Immigration_pro_ru.as_view(), name='immigration_pro'),
    path('visit/', mainapp_ru.Visit_ru.as_view(), name='visit'),
    path('life/', mainapp_ru.Life_ru.as_view(), name='life'),
    path('about/', mainapp_ru.About_ru.as_view(), name='about'),
    path('forms/', mainapp_ru.Forms_ru.as_view(), name='forms'),
    path('forms/cl_as_form', mainapp_ru.ClientAssesment_ru.as_view(), name='client_assesment_form'),
    path('forms/edu_form', mainapp_ru.Education_ru.as_view(), name='education_form'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
