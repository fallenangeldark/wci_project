from django.urls import path
import mainapp_ru.views as mainapp_ru

app_name = 'mainapp_ru'

urlpatterns =[
    path('', mainapp_ru.homeRu, name='home')
]
