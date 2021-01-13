from django.contrib import admin
from .models import Transaction, Chain

# Register your models here.
class TransactionFrom(admin.ModelAdmin):
	fields = ['liver', 'title', 'startdatetime', 'stream_url', 'onair', 'audience']

admin.site.register(Transaction, TransactionFrom)

class ChainFrom(admin.ModelAdmin):
	fields = ['index', 'transactions', 'previous_hash']

admin.site.register(Chain, ChainFrom)