from django.contrib import admin
from .models import HomeRu, InnerHomeRu
from mainapp_en.models import HomeEn, InnerHomeEn


# Register your models here.

admin.site.register(HomeRu)
admin.site.register(HomeEn)
admin.site.register(InnerHomeRu)
admin.site.register(InnerHomeEn)
