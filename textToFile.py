import os

def textToFile(title,text):
	if not os.path.exists("DownloadedText"):
		os.mkdir("DownloadedText")
		os.chdir("DownloadedText")
	else:
		os.chdir("DownloadedText")
	if not os.path.exists(title):
		os.mkdir(title)	
	os.chdir(title)
	title = title + ".txt"
	f = open(title,"w+")
	f.write(text)
	f.close()

