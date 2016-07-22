
class Counter:
	def __init__(self,counter=0):
		self.counter=counter
	def show(self):
		print self.counter
	def increment(self):
		self.counter+=1
	def decrement(self):
		self.counter-=1
	def __str__(self):
		return 'Counter:'+str(self.counter)

c = Counter()
c.show() # prints 0.
c.increment()
c.show() # prints 1
c.decrement() 
c.show() # prints 0
print c # prints 'Counter: 0' (implement the __str__ method)
c = Counter(10) # __init__ should accept an argument
c.show() # prints 10


