from django.shortcuts import render
from .models import Transaction, Chain
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
import json, hashlib
# Create your views here.

#Blockchain Core
class Blockchain_Core:
	#Vtuberの生放送データをブロックチェーンで保持
	def __init__(self):
		self.chain = Chain.objects.all()
		self.current_transactions = Transaction.objects.all()
		#ジェネシスブロック(一番最初のブロック)を生成
		#self.new_block(previous_hash=1)

	def new_block(self, previous_hash=None):
		#チェーンに新しいブロックを加える
		index = len(self.chain) + 1
		
		snippets = Chain.objects.last()
		previous_block = {'index':snippets.index,
						  'timestamp':str(snippets.timestamp),
						  'transactions': snippets.transactions,
						  'previous_hash': snippets.previous_hash}
		p_hash = previous_hash or self._hash(previous_block)
		#self.current_transactions = []

		transactions = []
		for t in self.current_transactions:
			transaction = {'liver':t.liver,
						   'title':t.title,
						   'startdatetime':t.startdatetime,
						   'stream_url':t.stream_url,
						   'onair':t.onair,
						   'audience':t.audience}
			transactions.append(transaction)

		chain_objects = Chain(index=index, transactions=str(transactions), previous_hash=p_hash)
		chain_objects.save()

		Transaction.objects.all().delete()		
		return chain_objects

	def new_transaction(self, liver, title, startdatetime, stream_url, onair, audience):
		#新しいトランザクションをリストに加える
		"""
		transaction(格納するデータ、つまりVtuberの生放送データ){
			'liver':{'uid': 'uid',
				     'livername': 'name',
				     'production': 'production',
				     'gender': 'gender'},
			'title': title,
			'startdatetime': datetime,
			'stream_url' : url,
			'onair': <bool>, #True=放送中,False=リマインド
			'audience': <int>
		}
		"""
		transaction = Transaction(
								liver=liver,
								title=title,
								startdatetime=startdatetime,
								stream_url=stream_url,
								onair=onair,
								audience=audience)
		transancion.save()

		return True

	@staticmethod
	def _hash(block):
		#ブロックをハッシュ化
		block_string = json.dumps(block, sort_keys=True).encode()
		return hashlib.sha256(block_string).hexdigest()

	@property
	def last_block(self):
		#最後のブロックをリターンする
		return self.chain[-1]

blockchain = Blockchain_Core()

class MiningView(APIView):
	def get(self, request, format=None):
		block = blockchain.new_block()
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
		serializer = ChainSerializer(snippets, many=True)
		return Response(serializer.data, status=status.HTTP_201_CREATED)