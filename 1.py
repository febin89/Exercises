#!/usr/bin/python

def print_urls(file):
    #Each line is of the form: GET /foo/bar/a.jpg
    #remove the GET and print only /foo/bar/a.jpg

    #use a for-loop to iterate through each line of `file'
    #split the line and print second part
	g=open('2.txt','w')
	for line in f:
		s=line.split(' ')
		g.write(s[1])
	g.close()

f = open('1.txt')
print_urls(f)
f.close()
 


   
