""" Implementation of a queue (FIFO) data structure """

class Queue:
	def __init__(self):
		self.qList = []

	def add(self, item):
		self.qList.append(item)

	def delete(self):
		item_to_del = self.qList[0]
		del self.qList[0]
		return item_to_del

	def size(self):
		return len(self.qList)

	def getQueue(self):
		return self.qList

""" Testing

queue = Queue()
queue.add(10)
queue.add(20)
queue.add(30)
queue.add(40)

print("Start queue: ", queue.getQueue())
print("Delete: ", queue.delete())
print("current queue: ", queue.getQueue())
print("current size: ", queue.size())
print("Delete: ", queue.delete())
print("current queue: ", queue.getQueue())

"""

