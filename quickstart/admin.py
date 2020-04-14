from django.contrib import admin
from .models import data, region, impact, severeImpact

admin.site.register(data)
admin.site.register(region)
admin.site.register(impact)
admin.site.register(severeImpact)

