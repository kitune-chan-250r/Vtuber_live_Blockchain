from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('liver', 'title', 'startdatetime', 'stream_url', 'onair', 'audience')
