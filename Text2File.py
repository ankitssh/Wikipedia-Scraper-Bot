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
<<<<<<< HEAD
	f = open(title,"wb")
	f.write(text.encode("utf8"))
=======
	f = open(title,"w+")
	f.write(text)
>>>>>>> 1506d748d356decd3d5b5b1b7ea6d9f55bf22be9
	f.close()

