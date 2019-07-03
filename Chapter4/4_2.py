class Node:
	def __init__(self, data, right, left):
		self.data = data
		self.right = right
		self.left = left

def create_binary_tree(L):
	if len(L) < 1:
		return None
	mid = len(L)//2
	left = create_binary_tree(L[:mid])
	right = create_binary_tree(L[mid+1:])
	return Node(L[mid], left, right)
