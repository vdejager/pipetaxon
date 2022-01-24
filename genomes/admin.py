from django.contrib import admin

# Register your models here.

from genomes.models import AssemblySummary, ANI_report_prokaryotes, Prokaryotes

class AssemblySummaryAdmin(admin.ModelAdmin):
    pass

admin.site.register(AssemblySummary, AssemblySummaryAdmin)

class ANI_report_prokaryotesAdmin(admin.ModelAdmin):
    pass

admin.site.register(ANI_report_prokaryotes, ANI_report_prokaryotesAdmin)

class ProkaryotesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Prokaryotes, ProkaryotesAdmin)