import re

def textCleaner(myString):
  
   
   
    myString= re.sub(r"\*\*","",myString)
    myString= re.sub(r"\[[a-z]\]","",myString)
    myString= re.sub(r"\[([0-9]|[0-9][0-9])\]","",myString)
    myString= re.sub(r"([_\?])","",myString)
    myString= myString.replace('("',"'")
    myString= myString.replace('")',"'")
        
    myString= re.sub(r'\(\/(.|\n)*?\)',"",myString)
    myString= re.sub(r"(\"(.|\n)+?\"[ |\n]\))","",myString)
    myString= re.sub(r"\[\[[a-zA-Z0-9]*\]\]","",myString)
    myString= re.sub(r"\[|\]"," ",myString)
    return myString


def titleCleaner(myString):
     myString= re.sub("[*]","",myString)
     myString=re.sub("[_]"," ",myString)
     return myString
    
    