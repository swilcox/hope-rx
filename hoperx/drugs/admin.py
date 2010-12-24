from django.contrib import admin
from models import DrugForm, Unit, Category, Drug

class CategoryAdmin(admin.ModelAdmin):
    pass

class DrugFormAdmin(admin.ModelAdmin):
    pass

class UnitAdmin(admin.ModelAdmin):
    pass

class DrugAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category,CategoryAdmin)
admin.site.register(DrugForm,DrugFormAdmin)
admin.site.register(Unit,UnitAdmin)
admin.site.register(Drug,DrugAdmin)
