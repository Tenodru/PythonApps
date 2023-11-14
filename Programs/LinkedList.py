
class Link (object):
	def _init__ (self, data, next = None):
		self.data = data
		self.next = next


class Linkedlist (object):
	def _init__ (self):
		self.first = None

	# add an item to the beginning of the list
	def insert_first (self, data):
		new_link = Link (data)

		new_link.next = self.first
		self.first = new_link

	# add an item to the end of the list
	def insert_last (self, data):
		new_link = Link (data)

		current = self.first
		if (current == None):
			self.first = new_link
			return

		while (current.next != None):
			current = current.next

		current.next = new_link

	# find an item in the LinkedList
	def find_link (self, data):
		current = self.first

		if (current == None):
			return None

		while (current.data != data):
			if (current.next == None):
				return None
			else:
				current = current.next

		return current

	#delete a link with given data
	def delete_link (self, data):
		previous = self.first
		current = self.first

		if (current == None):
			return None

		while (current.data != data):
			if (current.next == None):
				return None
			else:
				previous = current
				current = current.next

		if (current == self.first):
			self.first = self.first.next
		else:
			previous.next = current.next

		return current