from Scraper import ScrapperClass
import Text2File

#cleaner File remains to be used

sc= ScrapperClass()
myurl=sc.getUrl()
myreq=sc.getRequestToTheUrl(myurl)
sc.scrapedContent(myreq)
title=sc.getTitle()
paragraph=sc.getParagraph()

Text2File.Text2File(title,paragraph)
