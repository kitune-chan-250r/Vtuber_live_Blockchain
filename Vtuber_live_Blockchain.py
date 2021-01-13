class Vtuber_live_Blockchain:
	#Vtuberの生放送データをブロックチェーンで保持
	def __init__(self):
		self.chain = []
		self.current_transactions = []

	def new_block(self):
		#チェーンに新しいブロックを加える
		pass

	def new_transaction(self):
		#新しいトランザクションをリストに加える
		pass

	@staticmethod
	def _hash(block):
		#ブロックをハッシュ化
		pass

	@property
	def last_block(self):
		#最後のブロックをリターンする
		pass