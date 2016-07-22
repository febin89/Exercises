# A complex number class

class MyComplex:
    def __init__(self,re,im):
	self.re=re
	self.im=im
    def __str__(self):
	return str(self.re)+'+'+str(self.im)+'j'
    def __add__(self,num):
	ans=MyComplex(0,0)
	ans.re=self.re+num.re
	ans.im=self.im+num.im
	return ans
c = MyComplex(1, 2) 
d = MyComplex(3, 4)
#e = c.add(d)
print c.re, c.im # prints 4, 6

print c # prints (4 + 6j) # implement the __str__ method

e = c + d # implement the __add__ method

print e 

