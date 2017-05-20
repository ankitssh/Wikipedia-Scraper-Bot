import os

def Text2File(title,text):
	if not os.path.exists("DownloadedText"):
		os.mkdir("DownloadedText")
		os.chdir("DownloadedText")
	else:
		os.chdir("DownloadedText")
	if not os.path.exists(title):
		os.mkdir(title)	
	os.chdir(title)
	title = title + ".txt"

	try:
		f = open(title,"wb")
		f.write(text.encode("utf8"))
	except IOError:
		print("Error Writing The File")
	
	f.close()

	

