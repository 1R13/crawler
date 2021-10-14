class Url:
	
	def __init__(self, name: str, flag: int = 0):
		self.name = name
		self.flag = flag or 0
		self.search_hit = False

"""
0 = seen
1 = scheduled
2 = scanned
3 = unreachable
4 = forbidden
"""