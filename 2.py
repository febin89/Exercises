#!/usr/bin/python

def eliminate_duplicates_and_print_sorted(file):
    #remove duplicate lines from `file' and print the sorted lines
    #hint: you can use a set and also the "sorted" function
	s=set()
	
	for line in file:
		s.add(line)
	sort=sorted(s)
	f=open('3.txt','w')
	for l in sort: 
		f.write(l)
	f.close()
if __name__ == '__main__':
    eliminate_duplicates_and_print_sorted(open('2.txt'))
    
