import requests
import time

url = "http://data.fixer.io/api/latest?access_key=23a38fb98b0b297edb241f8e4a80119c&format=1"

data = requests.get(url)

json_data = data.json()

birinci_doviz= input("1. Dövizi Yazınız...")
ikinci_doviz= input("2. Dövizi Yazınız...")
miktar = float(input("Miktarı giriniz"))

print("Hesaplanıyor Lütfen bekleyiniz...")
time.sleep(1)
birim_sonuc=  json_data["rates"][ikinci_doviz] / json_data["rates"][birinci_doviz]

sonuc = birim_sonuc*miktar

print("{} {} = {} {}'dir".format(miktar,ikinci_doviz,sonuc,birinci_doviz,sonuc))

