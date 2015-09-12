#encoding:utf8
import requests
from BeautifulSoup import BeautifulSoup
import time
import os
import winsound
url = "https://www.ccxp.nthu.edu.tw/ccxp/COURSE/JH/7/7.2/7.2.7/JH727002.php"
acixstore = "your acix code, not mine"

headers = {
    "Accept"          : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding" : "gzip, deflate",
    "Accept-Language" : "zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4",
    "Cache-Control"   : "max-age=0",
    "Connection"      : "keep-alive",
#    "Content-Length"  : 71,
    "Content-Type"    : "application/x-www-form-urlencoded",
    "Host"            : "www.ccxp.nthu.edu.tw",
    "Origin"          : "https://www.ccxp.nthu.edu.tw",
    "Referer"         : "https://www.ccxp.nthu.edu.tw/ccxp/COURSE/JH/7/7.2/7.2.7/JH727001.php?ACIXSTORE=" + acixstore,
    "Upgrade-Insecure-Requests": "1",
    "User-Agent"      : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
}


data = "ACIXSTORE=" + acixstore + "&select=CS&act=1&Submit=%BDT%A9w+go"
req_url = url + "ACIXSTORE=" + acixstore

while True:

    print 'post request...'
    response = requests.post( url, headers=headers, data=data)
    response.encoding = 'big5'

    soup = BeautifulSoup(response.text)
    cols = soup.findAll('div', attrs={"align" : "center"})
    
    for x in cols:
        if x.renderContents() != '金仲達<br />KING, CHUNG-TA':
            continue
        
        i = cols.index(x)
        limit   = cols[i + 2].renderContents()
        current = cols[i + 3].renderContents()

        if limit == current:
            print 'full'
            print limit
            print current
            # for mac
            #os.system('say "your program has finished"')
        else:
            print 'go get it now!'
            winsound.Beep(300,2000)
            # for mac
            #os.system('say "your program has finished"')
        break
       
    print 'wait 3 secs...'
    time.sleep(3) 
