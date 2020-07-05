import sys, heapq
from functools import total_ordering
class Node:
    def __init__(self, frequency, character=None):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None
        

    def set_character(self,character):
        self.character = character

    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right

    def has_left_child(self):
        return self.left is not None
    
    def has_right_child(self):
        return self.right is not  None

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __ne__(self, other):
        return self.frequency != other.frequency

    def __lt__(self, other):
        return self.frequency < other.frequency    

    def __repr__(self):
        return "%s : %d" % (self.character, self.frequency)

class HuffmanTree():
    def __init__(self,node):
        self.root = node
    
    def get_root(self):
        return self.root

    


def huffman_encoding(data):

    if data == None or data == '':
        print('Empty string cannot be encoded')
        return '', None

    char_frequency = {}
    list_nodes = []
    for character in data:
        if char_frequency.get(character) is not None:
            char_frequency[character] += 1
        else:
            char_frequency[character] = 1


    

    for key, value in char_frequency.items():
        node = Node(value, key)        
        list_nodes.append(node)


    heapq.heapify(list_nodes)

    if len(list_nodes) ==1:        
        node = heapq.heappop(list_nodes)
        new_node = Node(node.frequency ) 
        new_node.set_left_child(node)
        new_node.set_right_child(Node(0))
        heapq.heappush(list_nodes, new_node)
        

    while len(list(list_nodes)) > 1:
        node1 = heapq.heappop(list_nodes)
        node2 = heapq.heappop(list_nodes)        
        new_node = Node(node1.frequency + node2.frequency)        
        new_node.set_left_child(node1)        
        new_node.set_right_child(node2)
        heapq.heappush(list_nodes,new_node) 

    root = heapq.heappop(list_nodes)    

    code_table = {}
    encode(root, "", code_table)
    encoded_data = ""

    
    for character in data:        
        encoded_data += code_table[character]
        


    return encoded_data, root
    

def encode(node, current_text, code_table):
    
    if node is not None:
        if node.character is not None:
          code_table[node.character] = current_text
        encode(node.left, current_text + "0", code_table)
        encode(node.right, current_text + "1", code_table)




def huffman_decoding(data,tree):
    if data == None or data == '':        
        return ''
    current_node = tree
    decoded_data = ""
    for bit in data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.left is None and current_node.right is None:            
            decoded_data += current_node.character
            current_node = tree
    return  decoded_data 


if __name__ == "__main__":
    codes = {}

    # Test case 1
    
    a_great_sentence = "The bird is the word"
    

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))    

    
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    # Test case 2

    a_great_sentence = ""      
    encoded_data, tree = huffman_encoding(a_great_sentence)
    

    # Test case 3

    a_great_sentence = "aaaaa"
    

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))    

    
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print(encoded_data)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    
    