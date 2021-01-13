import hashlib
import json
from time import time

class Vtuber_live_Blockchain:
	#Vtuberの生放送データをブロックチェーンで保持
	def __init__(self):
		self.chain = []
		self.current_transactions = []

		#ジェネシスブロック(一番最初のブロック)を生成
		self.new_block(previous_hash=1)

	def new_block(self, previous_hash=None):
		#チェーンに新しいブロックを加える
		block = {
			'index': len(self.chain) + 1,
			'timestamp' : time(),
			'transactions': self.current_transactions,
			'previous_hash': previous_hash or self._hash(self.chain[-1])
		}

		self.current_transactions = []
		self.chain.append(block)
		return block

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
		self.current_transactions.append({
			'liver': liver,
			'title': title,
			'startdatetime': startdatetime,
			'stream_url' : stream_url,
			'onair': onair,
			'audience': audience
		})

		return self.last_block['index'] + 1

	@staticmethod
	def _hash(block):
		#ブロックをハッシュ化
		block_string = json.dumps(block, sort_keys=True).encode()
		return hashlib.sha256(block_string).hexdigest()

	@property
	def last_block(self):
		#最後のブロックをリターンする
		return self.chain[-1]


