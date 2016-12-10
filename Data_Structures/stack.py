""" Implementation of a stack (FILO) data structure """

class Stack:
	def __init__(self):
		self.sList = []
		self.top = 0

	def size(self):
		return self.top

	def is_empty(self):
		return(self.top == 0)

	def push(self, item):
		if self.top < len(self.sList):
			self.sList[self.top] = item
		else:
			self.sList.append(item)

		self.top += 1	

	def pop(self):
		if self.is_empty():
			return None
		else:
			self.top -= 1
			return self.sList[self.top]



stack = Stack()
stack.push(10)
print('pushing 10...')
stack.push(20)
print('pushing 20...')
stack.push(30)
print('pushing 30...')
print('size : ', stack.size())
print('pop : ', stack.pop())
print('pop : ', stack.pop())
stack.push(40)
print('pushing 40...')
print('size : ', stack.size())
print('pop : ', stack.pop())
print('pop : ', stack.pop())
print('size : ', stack.size())

