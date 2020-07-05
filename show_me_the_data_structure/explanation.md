# Problem 1: LRU Cache

- I have used combination of Hashmap (python dictionary) and DoublyLinkedList to implement the LRU cache.
- The least recently used item can be at the trailing tail of the linked list. If you always remove and prepend the item to the list, head will  have the most recently used item. Thus if you reached the capacity, you simply pop off the tail and keep going.
- HashMap offers 𝑂(1)  time complexity for both put and get operations. It is used to retrieve values from the linkedlist quickly without having to actually traverse it.
- Get and set operations are constant time. Space complexity consist of linked list and cache dictionary, so Big O is O(2n)



- Time Complexity: O(1) Space Complexity: O(n)

# Problem 2: File Recursion

- The function return the list of paths to the matched file.
- The time complexity is Big O of n times the number of directories, since for each directory we call our function again. O(n)

The space complexity is O(n)

# Problem 3: Huffman Coding

The time complexity of the Huffman algorithm is O(nlogn). Using a heap to store the weight of each tree, each iteration requires O(logn) time to determine the cheapest weight and insert the new weight. There are O(n) iterations, one for each item.

# Problem 4: Active directory

Big O Notation Time & Space: O(n) No matter the size of users and groups, we have to search through them all recursively to find our user. We use two arrays to store our users and groups, so our Big O grows as simple multiples of these for space.

# Problem 5 - BlockChain
Our Blockchain problem is really just a node and a linked list. Each node in the list points to the next, while also storing the hash of itself, and its previous hash.

Since we merely iterate through a linked list, and do some hashing functions, the Big O for time should be a simple O(1). And Big O for space is 1 for our hash sha and 1 for our linked list: O(2n). Big O Notation Time: O(1) Space: O(n)

Problem 6 - Union and Intersection
The union function has two while loops, one for each linked list. Therefor its performance is Big O of N times 2: O(2n) or O(n).

The intersection function has a loop within a loop, checking for identical values in either list. It's performance is thus a bit worse at Big O of N squared: O(n**2).

In both functions I use Python's set function to create a unique cache list of either the union or intersection of the items in both lists. This adds another loop for iterating thru the final set, but it's effect on performance is minimal. With a linked list and a cache set, we have a space Big O of O(2n).

Big O Notation Time: O(n**2) Space: O(n)