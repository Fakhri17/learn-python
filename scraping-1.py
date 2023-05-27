import requests
from bs4 import BeautifulSoup
import re

res = requests.get('https://simasinsurtech.com/layanan/bengkel-authorized-asuransi-simasinsurtech/')
soup = BeautifulSoup(res.text, 'html.parser')

rows = soup.find_all('tr')

for row in rows:
    # scrape by data-label
    kotaBengkel = row.find('td', {"data-label": "Kota"})
    namaBengkel = row.find('td', {"data-label": "Nama Bengkel"})
    alamatBengkel = row.find('td', {"data-label": "Alamat"})
    nomorTelepon = row.find('td', {"data-label": "No.Telpon"})
    
    if kotaBengkel and kotaBengkel.text and namaBengkel and alamatBengkel and nomorTelepon:
        print("Kota Bengkel: " + kotaBengkel.text)
        print("Nama Bengkel: " + namaBengkel.text)
        print("Alamat Bengkel: " + alamatBengkel.text)
        print("Nomor Telepon: " + nomorTelepon.text)
        print("\n")
