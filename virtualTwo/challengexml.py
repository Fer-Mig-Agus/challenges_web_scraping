import requests
from rich import print
from lxml import etree

def get_data(url):
    print(url)
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0'
    }
    
    response=requests.get(url,headers=headers,timeout=10)

    tree = etree.fromstring(response.content)
    
    print(etree.tostring(tree, pretty_print=True, encoding="utf-8").decode("utf-8"))



if __name__=='__main__':
    url='https://www.diariopanorama.com/rss/news?token=llo387fg12fu54ks'
    data=get_data(url)
    #print(data)