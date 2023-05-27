import requests
from bs4 import BeautifulSoup
import re


res = requests.get('https://lifepal.co.id/media/bengkel-mobil-surabaya/')
soup = BeautifulSoup(res.text, 'html.parser')

rows = soup.find_all('tr')

for row in rows:
    # print tr td
    span_elements = row.find_all('span')
    if len(span_elements) >= 2:
        namaBengkel = span_elements[0].text
        alamatBengkel = span_elements[1].text
        pattern = r"\d{5}\s*–\s*\d{4}\s*\d{4}"
        match = re.search(pattern, alamatBengkel)
        print("Nama Bengkel: " + namaBengkel)
        print("Alamat Bengkel: " + alamatBengkel)
        if match:
            print("Nomor Telepon: " + match.group(0))
        else:
            print("Nomor Telepon: -")
        print("\n")
        
    else:
        print("error")