import os
import requests
from bs4 import BeautifulSoup

page = 1
URL = input("URL 써주세요: ")
#dir_name = input("폴더 이름을 써주세요: ")
re_URL = requests.get(URL)
html = re_URL.text
soup = BeautifulSoup(html, 'html.parser')
#os.mkdir(dir_name)

img = soup.find("div",{"class":"wt_viewer"})
print(img)
img2 = img.find_all("img")

for img_src in img2:
    img_url = img_src['src']
    #os.system(f'curl -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36" {img_url} > ./{dir_name}/{page}.jpg')
    page +=1
