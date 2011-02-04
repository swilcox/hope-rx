from django.contrib import admin

from inventory.models import Lot, Transfer, TransferDetail, Adjustment, Dispense


class LotAdmin(admin.ModelAdmin):
    pass


class TransferAdmin(admin.ModelAdmin):
    pass


class TransferDetailAdmin(admin.ModelAdmin):
    pass


class AdjustmentAdmin(admin.ModelAdmin):
    pass


class DispenseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Lot,LotAdmin)
admin.site.register(Adjustment,AdjustmentAdmin)
admin.site.register(Transfer,TransferAdmin)
admin.site.register(TransferDetail,TransferDetailAdmin)
admin.site.register(Dispense,DispenseAdmin)

