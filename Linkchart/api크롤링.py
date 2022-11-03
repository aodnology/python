import urllib.request
import datetime
import json

# 발급받은 api id,secret
id = ""
secret = ""

def getRequestUrl(url):
    req = urllib.request.Request(url) 
    req.add_header("Id", id)
    req.add_header("secret", secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URl : %s" %(datetime.datetime.now(), url))
        return None