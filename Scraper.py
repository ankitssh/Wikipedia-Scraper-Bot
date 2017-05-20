try:
    from bs4 import BeautifulSoup
    import requests,html2text,validators
except ImportError:
    print("Please instll BeautifulSoup,Requests,Html2Text,Validators Module.")
    print(input())

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

    @staticmethod
    def validateUrl(url):
        try:
            return bool(validators.url(url).public)
        except Exception as e:
            isWiki = url.find("wikipedia.org")
            if(isWiki != -1):
                return True
            else:
                return False



