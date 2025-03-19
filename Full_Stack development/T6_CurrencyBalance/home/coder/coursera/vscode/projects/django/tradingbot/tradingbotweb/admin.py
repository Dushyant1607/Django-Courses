from django.contrib import admin
from .models import Currency, Transaction, CurrencyHistory

# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = ('exchange_date',)
class CurrencyHistoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

admin.site.register(Currency)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(CurrencyHistory, CurrencyHistoryAdmin)
