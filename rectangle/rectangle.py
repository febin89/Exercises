class Rectangle:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
		
	def smaller(self,other):
		area1=self.length*self.breadth 
		area2=other.length*other.breadth
		if area1<area2:
			return 'smaller' 
		else:
			return 'bigger'
	def __lt__(self,other):
		area1=self.length*self.breadth
		area2=self.length*self.breadth
		if area1<area2:
			return 'smaller'
		else:
			return 'bigger'
a = Rectangle(3, 4)

b = Rectangle(4, 5)

# prints True
print a.smaller(b)

# prints False
print b < a
