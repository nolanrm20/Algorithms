""" Implementation of a linked list """ 

class Node:
	def __init__(self, item, next):
		self.item = item
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def add(self, item):
		self.head = Node(item, self.head)

	def remove(self):
		if self.is_empty():
			return None
		else:
			ret_item = self.head.item
			self.head = self.head.next()
			return ret_item

	def is_empty(self):
		return self.head == None
