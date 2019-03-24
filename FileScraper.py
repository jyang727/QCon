import urllib.request, urllib.parse, urllib.error
import re

def getLinks(url):
    html = urllib.request.urlopen(url).read()
    pdflinks = re.findall(b'href="(http|https://.*pdf)"', html)
    pptxlinks = re.findall(b'href="(http|https://.*pptx)"', html)
    return pdflinks + pptxlinks

def doDownload(url, filepath):
    i = url.rindex('/')
    filename = url[i+1:len(url)]
    content = urllib.request.urlopen(url).read()
    fhand = open(filepath + filename, 'wb')
    fhand.write(content)
    fhand.close()

qconurl = 'https://qconsf.com/schedule/sf2018/tabular'
filepath = '/home/jyang/QConTest/'
links = getLinks(qconurl)

print('Download started...')
for link in links:
    if (len(link)>0):
        doDownload(link.decode("utf-8"), filepath)
print("Download of %d files completed." %len(links))