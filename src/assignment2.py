import requests
from bs4 import BeautifulSoup
req = requests.get('https://decrypt.co/83079/bitcoin-ethereum-dogecoin-rose-this-week')
file= open("D:\PYTHON\index.txt", "w", encoding='utf-8')
file.write(req.text)
file.close()

with open("D:\PYTHON\index.txt", encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

a = soup.find_all("p")


for x in a:
    print(x)