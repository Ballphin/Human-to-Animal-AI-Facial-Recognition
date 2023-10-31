from bs4 import BeautifulSoup
from urllib.request import urlopen
# Google Image Search got blocked by Google, so I changed the code to Naver Image Search
# Bing is a good alternative as well     
response = urlopen('https://www.naver.com/')
soup = BeautifulSoup(response, 'html.parser')
i = 1
f = open("새파일.txt", 'w')
for anchor in soup.select("span.ah_k"):
    data = str(i) + "위 : " + anchor.get_text() + "\n"
    i = i + 1
    f.write(data)
f.close()