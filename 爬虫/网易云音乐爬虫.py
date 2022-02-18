#encoding=utf8
import requests
from bs4 import BeautifulSoup
import urllib.request
headers = {
    'Referer':'http://music.163.com/',
    'Host':'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }
#play_url = 'http://music.163.com/playlist?id=317113395'
play_url = 'http://music.163.com/playlist?id=2182968685'
 
s = requests.session()
response=s.get(play_url,headers = headers).content
s = BeautifulSoup(response,'lxml')
main = s.find('ul',{'class':'f-hide'})
 
for music in main.find_all('a'):
    print('{} : {}'.format(music.text, music['href']))