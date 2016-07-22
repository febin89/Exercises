import requests,urllib

#save images to files.
#sorted and duplicates-removed urls
#are obtained from a file
g=[]
def print_urls(file):
    #Each line is of the form: GET /foo/bar/a.jpg
    #remove the GET and print only /foo/bar/a.jpg

    #use a for-loop to iterate through each line of `file'
    #split the line and print second part
        for line in file:
                s=line.split(' ')
                g.append(s[1])
        return g


def eliminate_duplicates_and_print_sorted(file):
    #remove duplicate lines from `file' and print the sorted lines
    #hint: you can use a set and also the "sorted" function
	f=open('1.txt','r')
	print_urls(f)
        s=set()

        for line in file:
                s.add(line)
        sort=sorted(s)
        f=open('3.txt','w')
        for l in sort:
                f.write(l)
        f.close()
#if __name__ == '__main__':
 #   eliminate_duplicates_and_print_sorted(g)

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

eliminate_duplicates_and_print_sorted(g)
main()
print '<html>'
print'\t<head><title>Images</title></head>\n\t<body>'
for i in range(20):
	print '\t\t<img src="'+str(i)+'.jpg">'
print '</body></html>'
