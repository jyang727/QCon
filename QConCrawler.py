import FileDownloader
import PageScraper

qconurl = 'https://qconsf.com/schedule/sf2018/tabular'
filepath = '/home/jyang/QCon2018/'

links = PageScraper.getLinks(qconurl)

print('Download started...')
for link in links:
    if (len(link)>0):
        print(link.decode("utf-8"))
        FileDownloader.doDownload(link.decode("utf-8"), filepath)

print("Download of %d files completed." %len(links))
