import requests
import requests.models


def getHTMLText(url):
    try:
        global r
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return " "
url = "https://www.baidu.com"
print(getHTMLText(url))
print(len(r.text))
print(r.content)

