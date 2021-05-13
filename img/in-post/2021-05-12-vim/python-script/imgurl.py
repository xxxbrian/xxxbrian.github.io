#%%
f=open("../../../../_posts/2021-05-12-vim的副本.md","r")
text=f.read()
f.close()

import re
from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def search_url(text):
    imgurl = re.compile("[a-zA-z]+://[^\s]*")
    res=imgurl.findall(text)
    return res

def download(url):
    print(url)
    a=url.split("/")
    print(a[len(a)-1])
    urlretrieve(url, './'+a[len(a)-1]) 

downloadlists=search_url(text)
for url in downloadlists:
    s=url.split(".")
    if s[len(s)-1]=="png)"or s[len(s)-1]=="jpg)":
        url=url.replace(")", "")
        print(url)
        download(url)
    else:
        print("erro:",url)

# %%
