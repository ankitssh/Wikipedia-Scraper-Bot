from Scraper import ScrapperClass
import Text2File

import Cleaner


sc= ScrapperClass()
myurl=sc.getUrl()

if(sc.validateUrl(myurl)):
	myreq=sc.getRequestToTheUrl(myurl)
	sc.scrapedContent(myreq)
	title=sc.getTitle()
	paragraph=sc.getParagraph()
	paragraph=Cleaner.textCleaner(paragraph)
	title=Cleaner.titleCleaner(title)
	Text2File.Text2File(title,paragraph)
else:
	print("Enter Correct Wikipedia Url")
	print(input())


