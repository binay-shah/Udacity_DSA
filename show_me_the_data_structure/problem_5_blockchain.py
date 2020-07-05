import hashlib
import datetime

class Block:

		def __init__(self, timestamp, data, previous_hash):
			self.timestamp = timestamp
			self.data = data
			self.previous_hash = previous_hash
			self.hash = self.calc_hash()
			self.next = None


		def calc_hash(self):
			sha = hashlib.sha256()
			hash_str = self.data.encode('utf-8')
			sha.update(hash_str)
			return sha.hexdigest()

		def __repr__(self):
			return str(self.timestamp) + str(" | ") + str(self.data) + str(" | ") + str(self.previous_hash) + str(" | ") + str(self.hash)


class BlockChain:
	def __init__(self):
		self.head = None
		self.tail = None

	def append_block(self, data):

		if data is None or data == "":
			return
		elif self.head is None:
			block = Block(datetime.datetime.utcnow(), data, 0)
			self.head = block
			self.tail = self.head
			return 
		else:
			self.tail.next = Block(datetime.datetime.utcnow(), data, self.tail.hash)
			self.tail = self.tail.next
			return

	def to_list(self):
		out_list = []
		block = self.head
		while block:
			out_list.append(block)
			block = block.next
		return out_list

def main():
		# Test Case 1
		bl = BlockChain()
		data1 = "First Blockchain block"
		data2 = "Second Blockchain block"
		data3 = "Third Blockchain block"
		bl.append_block(data1)
		bl.append_block(data2)
		bl.append_block(data3)
		print(bl.to_list()) # prints block chain

		bl1 = BlockChain()
		bl1.append_block("")
		bl1.append_block("")
		print(bl1.to_list())  # prints empty block chain as there was no data passed
		#Test Case 3
		bl2 = BlockChain()
		bl2.append_block(None)
		bl2.append_block(None)
		print(bl2.to_list())  # prints empty block chain as there was no data passed
	 


if __name__ == "__main__":
		main()

