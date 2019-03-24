import urllib.request, urllib.parse, urllib.error
import re

def getLinks(url):
    html = urllib.request.urlopen(url).read()
    pdflinks = re.findall(b'href="(http|https://.*pdf)"', html)
    pptxlinks = re.findall(b'href="(http|https://.*pptx)"', html)
    
    return pdflinks + pptxlinks
