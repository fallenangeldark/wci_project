from django.urls import path
import mainapp_ru.views as mainapp_ru

app_name = 'mainapp_ru'

urlpatterns =[
    path('', mainapp_ru.Main_ru.as_view(), name='home'),
    path('immigration/', mainapp_ru.Immigration_ru.as_view(), name='immigration'),
    path('visit/', mainapp_ru.Visit_ru.as_view(), name='visit'),
    path('life/', mainapp_ru.Life_ru.as_view(), name='life'),
    path('about/', mainapp_ru.About_ru.as_view(), name='about'),
]
