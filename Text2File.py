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

	f = open(title,"wb")
	f.write(text.encode("utf8"))


	f.close()

