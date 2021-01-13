from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Transaction
from .serializers import *

# Create your views here.

def mining(request):
	print('hello')

class TransactionViewSet(viewsets.ModelViewSet):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer


