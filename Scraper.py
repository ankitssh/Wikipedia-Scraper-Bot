from bs4 import BeautifulSoup
import requests,html2text

class ScrapperClass:
    title=""
    paragraph=""
   
    @staticmethod
    def getUrl():
        print("Enter the wikipedia URL to scrape")
        url=input()
        return url
    @staticmethod
    def getRequestToTheUrl(url):
        req=requests.get(url)
        return req
        
    
    def scrapedContent(self,req):
        sourceCode=BeautifulSoup(req.text,"html.parser")
        
        self.title=html2text.html2text(str(sourceCode.find("h1",{"id":"firstHeading"})))[2:]
        self.title=self.title.replace("\n\n","")
        paragraphRaw=str(sourceCode.find("div",{"id":"mw-content-text"}))
        try:
            startIndex=paragraphRaw.index("</table>\n<p>")
        except ValueError:
            startIndex=paragraphRaw.index("</div>\n<p>")
            
        
        endIndex=paragraphRaw.index('<div class="toc" id="toc">',startIndex)
        
        self.paragraph=html2text.html2text(paragraphRaw[startIndex:endIndex])
        
    def getTitle(self):
        return self.title
    def getParagraph(self):
        return self.paragraph
       


