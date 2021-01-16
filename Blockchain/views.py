from django.shortcuts import render
from .models import Transaction, Chain
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
import json
# Create your views here.


class MinigView(APIView):
	def get(self, request, format=None):
		#マイニング処理
		return Response(status=status.HTTP_201_CREATED)


class TransactionView(APIView):
    def get(self, request, format=None):
        snippets = Transaction.objects.all()
        serializer = TransactionSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
    	#トランザクション処理
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FullChainView(APIView):
	def get(self, request, format=None):
		snippets = Chain.objects.all()
		#response_chain = serializers.serialize('json', data)
		serializer = ChainSerializer(snippets, many=True)
		#response_chain = json.dumps([d.to_dict() for d in data])
		#print(response_chain)
		return Response(serializer.data, status=status.HTTP_201_CREATED)