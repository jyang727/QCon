import urllib.request, urllib.parse, urllib.error

def doDownload(url, filepath):
    i = url.rindex('/')
    filename = url[i+1:len(url)]

    content = urllib.request.urlopen(url).read()
    fhand = open(filepath + filename, 'wb')
    fhand.write(content)
    fhand.close()