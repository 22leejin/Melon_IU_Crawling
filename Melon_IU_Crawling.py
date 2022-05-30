import requests
from bs4 import BeautifulSoup
 
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0)'}
req = requests.get('https://www.melon.com/artist/album.htm?artistId=261143', headers = header)
html = req.text
parse = BeautifulSoup(html, 'html.parser')
 
titles = parse.find_all("div", {"class": "atist_info"})
songs = parse.find_all("dd", {"class": "wrap_btn"})
release_dates = parse.find_all("dd", {"class": "wrap_btn"})

title = []
song = []
release_date =[]

for t in titles:
  title.append(t.find('a').text)

for s in songs:
  song.append(s.find('span', {"class": "tot_song"}).text)

for r in release_dates:
  release_date.append(r.find('span').text)

print("  아이유 앨범정보 [최신순]")
for i in range(15):
  print('%3d - 앨범 이름: %s - %s - 앨범 발매일: %s'%(i+1, title[i], song[i], release_date[i]))