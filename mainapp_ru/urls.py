from django.urls import path
import mainapp_ru.views as mainapp_ru
from django.views.generic.base import RedirectView
# import mainapp_en.views as mainapp_en

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
]
