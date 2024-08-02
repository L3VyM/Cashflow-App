from django.contrib import admin
from .models import CashFlowSection, Transaction, CashFlowStatement

admin.site.register(CashFlowSection)
admin.site.register(Transaction)
admin.site.register(CashFlowStatement)
