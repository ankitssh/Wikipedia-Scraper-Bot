def textToFile(text):
	title = ""
	for t in text:
		if(t is not "\n"):
			title = title + t 
		else:
			break
	title = title + ".txt"
	f = open(title,"w+")
	f.write(text)
	f.close()