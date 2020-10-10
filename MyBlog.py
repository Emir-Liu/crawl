import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup
import re
import string

def findInternalLinks(obj,links):
    for link in obj.find_all('a'):
        #print(link)
        if link.attrs is not None:
            #print(link.attrs)
            if link.has_attr('href') :
                #print(link['href'])
                match_key = "^(http|www|/)"
                if link['href'] not in links and re.match(match_key,link['href']):
                    links.append(link['href'])
    return 0

url = "http://www.dfcj.net/"
links = []
links.append(url)
num_link = 0
while (num_link < len(links)):
    print('start...')
    #print('num_link:',num_link)
    #print("len_links",len(links))
    new_url = links[num_link]
    num_link = num_link + 1
    internal_key = "^(/)"
    external_key = "^(http|www)"

    if re.match(internal_key,new_url) or re.match(url,new_url):
        if not re.match(url,new_url):
            act_url = url+new_url
        else:
            act_url = new_url
        #下面的部分代码还有问题，中文url无法打开
        '''
        print('act_url',act_url)
        urllib.parse.quote(act_url,safe=string.printable)
        print('quote_act_url',act_url)
        '''
        #当url中有中文的时候需要使用上面的函数
        try:
            page = urllib.request.urlopen(act_url)
        except:
            print("could not open %s",act_url)
            continue
        html = page.read()
        obj = BeautifulSoup(html)
        findInternalLinks(obj,links)
    #print('end...')
    #print('links',links)
    print('num_link:',num_link)
    print("len_links",len(links))
print(links)
