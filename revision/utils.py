# Python3 program to merge sort of linked list

# create Node using class Node.
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	
	# push new value to linked list
	# using append method
	def append(self, new_value):
		
		# Allocate new node
		new_node = Node(new_value)
		
		# if head is None, initialize it to new node
		if self.head is None:
			self.head = new_node
			return
		current_node = self.head
		while current_node.next is not None:
			current_node = current_node.next
			
		# Append the new node at the end
		# of the linked list
		current_node.next = new_node
		
	def sortedMerge(self, node1, node2):
		result = None
		
		# Base cases
		if node1 == None:
			return node2
		if node2 == None:
			return node1
			
		# pick either a or b and recur..
		if node1.data <= node2.data:
			result = node1
			result.next = self.sortedMerge(node1.next, node2)
		else:
			result = node2
			result.next = self.sortedMerge(node1, node2.next)
		return result
	
	def mergeSort(self, head):
		
		# Base case if head is None
		if head == None or head.next == None:
			return head

		# get the middle of the list
		middle = self.getMiddle(head)
		next_to_middle = middle.next

		# set the next of middle node to None
		middle.next = None

		# Apply mergeSort on left list
		left = self.mergeSort(head)
		
		# Apply mergeSort on right list
		right = self.mergeSort(next_to_middle)

		# Merge the left and right lists
		sorted_list = self.sortedMerge(left, right)
		return sorted_list
	
	# Utility function to get the middle
	# of the linked list
	def getMiddle(self, head):
		if (head == None):
			return head

		slow = head
		fast = head

		while (fast.next != None and
			fast.next.next != None):
			slow = slow.next
			fast = fast.next.next
			
		return slow

# Utility function to get all value from the linked list
def get_unique_value_from_li(head):
	if head is None:
		return []
	temp=[]
	slow = head
	fast=head
	while fast:
		if fast.data==slow.data:
			fast=fast.next
		else:
			temp.append(slow.data)
			slow=fast
	temp.append(slow.data)
	return temp