import urllib2
import os 

# define url_pattern: www.something*.pdf
# define file_pattern: www.something*.pdf will be name into file file_pattern*.pdf
# define url_pattern_range: declare range for * (for example * in ['a','b','c'])
# define destinatation: where to place files

destination = "./Reinforcement Learning and Optimal Control/"

def url_pattern(index):
	return "https://web.mit.edu/dimitrib/www/Slides_Lecture"+index+"_RLOC.pdf"

def file_pattern(index):
	return "slides_"+index+".pdf"

url_pattern_range = [str(i) for i in range(1,14)]

# check that "try/except" is working (when accessing webpages that don't exist)
# url_pattern_range = [str(i) for i in range(0,2)]

#----------------------------------------------------------------#

def main():

	# check if "destination" directory exists, otherwise create it
	if not os.path.isdir(destination):
		os.makedirs(destination)
    	print("created directory " + destination)

	for index in url_pattern_range:
		url = url_pattern(index)
		download_pdf(destination, file_pattern(index), url)

def download_pdf(destination, file_name, download_url):
	try:
		response = urllib2.urlopen(download_url)
		
		file = open(destination+file_name, 'wb')
		file.write(response.read())
		file.close()
		print("download of " + file_name + " completed")
	
	except:
		print("could not access " + download_url)
    

if __name__ == "__main__":
    main()