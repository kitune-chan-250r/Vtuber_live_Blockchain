from rest_framework import serializers
from .models import Transaction, Chain

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('liver', 'title', 'startdatetime', 'stream_url', 'onair', 'audience')

class ChainSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chain
		fields = ('index', 'timestamp', 'transactions', 'previous_hash')
