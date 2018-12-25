from django.contrib import admin

from .models import HomeEn, InnerHomeEn, ClientAssesment, Education

# Register your models here.

admin.site.register(HomeEn)
admin.site.register(InnerHomeEn)
admin.site.register(ClientAssesment)
admin.site.register(Education)
