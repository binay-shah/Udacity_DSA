# Your work here

class DoubleNode:
	def __init__(self, key, value):
		self.value = value
		self.key = key
		self.next = None
		self.previous = None
		
		
class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
	
	def append(self, new_node):        
		# TODO: Implement this method to append to the tail of the list        
		if self.head is None:
			self.head = new_node
			self.tail = self.head
			return
			
		self.tail.next = new_node
		self.tail.next.previous = self.tail
		self.tail = self.tail.next
		return new_node
	
	def prepend(self, node):        
		if self.head is None:
			self.head = node
			self.tail = self.head
			
		else:
			node.next = self.head
			self.head.previous = node        	
			node.previous= None
			self.head = node

		

	def move_to_front(self, node):
		if self.head == node:
			return 
		if self.tail == node:
			self.tail = node.previous
		if node.previous is not None:
			node.previous.next  = node.next
			
		self.prepend(node)	  
			
	def delete_tail(self):
		if self.head is None:
			return 
		prev_node = self.tail.previous
		self.tail = prev_node
		prev_node.next = None
		
	def to_list(self):
		out_list = []
		node = self.head
		while node:
			out_list.append(node.value)
			node = node.next
		return out_list

class LRU_Cache(object):

	def __init__(self, capacity):
		# Initialize class variables
		self.capacity = capacity
		self.num_elements = 0
		self.cache = {}
		self.doubly_linked_list = DoublyLinkedList()

	def get(self, key):
		# Retrieve item from provided key. Return -1 if nonexistent. 
		node =  self.cache.get(key, None)

		if node is None:
			return -1
		self.doubly_linked_list.move_to_front(node)  
		print(self.doubly_linked_list.to_list())              
		return node.value
		

	def set(self, key, value):
		# Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
		if(self.capacity == 0):
			print('Cache size is 0. Cannot add elements')
			return 
		if self.cache.get(key, None) is not  None:
			node = self.cache.get(key)
			node.value = value
			self.doubly_linked_list.move_to_front(node) 
			return 
			
		new_node = DoubleNode(key, value)
		if(self.num_elements < self.capacity):            
			self.cache[key] = new_node 
					 
		else:
			node = self.doubly_linked_list.tail            
			self.cache[node.key] = None
			self.doubly_linked_list.delete_tail()
			self.num_elements -= 1  

		self.doubly_linked_list.prepend(new_node)
		self.num_elements += 1
		
		
			
		
		
# Test 1        
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))  
# 1    
print(our_cache.get(2))
# 2
print(our_cache.get(9))    # returns -1 because 9 is not present in the cache
# -1

our_cache.set(5, 5) 
our_cache.set(6, 6)


print(our_cache.get(3) )    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
# -1

# Test 2

our_cache = LRU_Cache(5)
our_cache.set(12343545, 1)
our_cache.set(564, 2)
our_cache.set(456, 3)
our_cache.set(678, 4)
print(our_cache.get(1))  # -1
print(our_cache.get(12343545) ) # 1
print(our_cache.get(564))  # 1
print(our_cache.get(678) ) # 1
our_cache.set(1, 564)
our_cache.set(1, 456)
our_cache.set(1, 678)
print(our_cache.get(1))  # 678

# Test 3

our_cache = LRU_Cache(0)
our_cache.set(1, 1)
our_cache.get(1)
