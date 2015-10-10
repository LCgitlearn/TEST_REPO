import urllib
import time
url = "http://www.rays-counter.com/d321_f6_007/56166a49f009f/"
i = 0
while(True):
    i += 1
    try:
        urllib.urlopen(url)
        print("ok" + str(i))
    except:
        print("error")
        time.sleep(5)
