class Pagination:
	def __init__(self, items, has_prev, has_next, next_num, prev_num, page, pages, total):
		self.items = items
		self.has_prev = has_prev
		self.next_num = next_num
		self.prev_num = prev_num
		self.page = page
		self.pages = pages
		self.has_next = has_next
		self.total = total
