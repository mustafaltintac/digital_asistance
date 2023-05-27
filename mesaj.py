from datetime import datetime
import requests
import time
ap = 'https://api.telegram.org/bot5622134571:AAGCLYvoNgjNJez1gut4oNgRFMs6EBZvw8E/getUpdates'
 
def acil_cagri(deger):
    print("çalıştı")
    zaman=datetime.now()
    saniye=zaman.strftime("%S")
    print(f"fonksiyon zamanı{saniye}")

    if(deger>80 and deger<90 ):
        time=int(datetime.now().strftime("%S"))
        print(f"sistem zamanı{time}")

        mesaj = f"Hastanın Durumu kritik seviyede acil yardım çağrısında buluun,Hastanızın oksijen değeriolması gerekenden düşük. Knadaki oksijen değeri:{deger}"
        response = requests.post(url="https://api.telegram.org/bot5622134571:AAGCLYvoNgjNJez1gut4oNgRFMs6EBZvw8E/sendMessage", data={"chat_id":"1018753509", "text": mesaj}).json()
        
    elif(deger<80 and deger>50):
        if(deger>=75 ):
            mesaj = f"Hastanın Durumu kritik seviyede acil yardım çağrısında buluun,Hastanızın nabız değeri olması gerekenden yüksek. Hastanın nabız değeri:{deger}"
            response = requests.post(url="https://api.telegram.org/bot5622134571:AAGCLYvoNgjNJez1gut4oNgRFMs6EBZvw8E/sendMessage", data={"chat_id":"1018753509", "text": mesaj}).json()
        if(deger<=59 ):
            mesaj = f"Hastanın Durumu kritik seviyede acil yardım çağrısında buluun,Hastanızın nabız değeri olması gerekenden düşük. Hastanın nabız değeri:{deger}"
            response = requests.post(url="https://api.telegram.org/bot5622134571:AAGCLYvoNgjNJez1gut4oNgRFMs6EBZvw8E/sendMessage", data={"chat_id":"1018753509", "text": mesaj}).json()
    if(deger<45 and deger>37.9):
        mesaj = f"Hastanın Durumu kritik seviyede acil yardım çağrısında buluun,Hastanızın vucüt sıcaklık değeri olması gerekenden yüksek havale olma ihtimali var.Vücut sıcaklık değeri:{deger}"
        response = requests.post(url="https://api.telegram.org/bot5622134571:AAGCLYvoNgjNJez1gut4oNgRFMs6EBZvw8E/sendMessage", data={"chat_id":"1018753509", "text": mesaj}).json()
        