from django.urls import path
import mainapp_en.views as mainapp_en
# import mainapp_ru.views as mainapp_ru

app_name = 'mainapp_en'

urlpatterns =[
    path('', mainapp_en.Main_en.as_view(), name='home'),
    path('immigration/', mainapp_en.Immigration_en.as_view(), name='immigration'),
    path('visit/', mainapp_en.Visit_en.as_view(), name='visit'),
    path('life/', mainapp_en.Life_en.as_view(), name='life'),
    path('about/', mainapp_en.About_en.as_view(), name='about'),
]
