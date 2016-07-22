#!/usr/bin/python

import requests,urllib

#save images to files.
#sorted and duplicates-removed urls
#are obtained from a file
def save_image(url, filename):
    #url is the complete url of the image
    #and filename is the name of the file to save
    #the image to
	print url
    	urllib.urlretrieve(url,filename)
	#f=open(filename,'wb')
	#shutil.copyfileobj(r.raw,f)
	#f.write(r.content)
	#f.close()



def main():

    filename = 0
    url_base = 'http://code.google.com'

    #open file 3.txt
    for url in open('3.txt'):
	save_image(url_base+url,str(filename)+'.jpg')
	filename+=1
    


    #using a for loop, save each url to a file
    #you can use the save_image function for doing 
    #this.
    #The files to which you are saving the urls should
    #be called 0.jpg, 1.jpg, 2.jpg etc.
    
   


main()
