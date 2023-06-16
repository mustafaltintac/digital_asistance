from datetime import datetime
import requests
import time
ap = 'https://api.telegram.org/bot5622134571:AAGCLYvoNgjNJez1gut4oNgRFMs6EBZvw8E/getUpdates'

def yüksek_nabiz(besin_1,besin_2,besin_3,besin_4):
    mesaj=f"{besin_1},{besin_2},{besin_3},{besin_4}-->> bu besinler hastanızın nabız değerini artırmaktadır"
    response = requests.post(url="https://api.telegram.org/bot5622134571:AAGCLYvoNgjNJez1gut4oNgRFMs6EBZvw8E/sendMessage", data={"chat_id":"1018753509", "text": mesaj}).json()

def dusuk_nabiz(besin_1,besin_2,besin_3,besin_4):
    mesaj=f"{besin_1},{besin_2},{besin_3},{besin_4}-->> bu besinler hastanızın nabız değerini düşürmektedir"
    response = requests.post(url="https://api.telegram.org/bot5622134571:AAGCLYvoNgjNJez1gut4oNgRFMs6EBZvw8E/sendMessage", data={"chat_id":"1018753509", "text": mesaj}).json()

def yuksek_ates(besin_1,besin_2,besin_3,besin_4):
    mesaj=f"{besin_1},{besin_2},{besin_3},{besin_4}-->> bu besinler hastanızın ateşlenmesine neden olmaktadır"
    response = requests.post(url="https://api.telegram.org/bot5622134571:AAGCLYvoNgjNJez1gut4oNgRFMs6EBZvw8E/sendMessage", data={"chat_id":"1018753509", "text": mesaj}).json()

def yuksek_nabiz_ilac(ilac_1,ilac_2,ilac_3,):
    mesaj=f"{ilac_1},{ilac_2},{ilac_3}-->> bu ilaclar hastanızın nabız değerini artırmaktadır"
    response = requests.post(url="https://api.telegram.org/bot5622134571:AAGCLYvoNgjNJez1gut4oNgRFMs6EBZvw8E/sendMessage", data={"chat_id":"1018753509", "text": mesaj}).json()

def dusuk_nabiz_ilac(ilac_1,ilac_2,ilac_3,):
    mesaj=f"{ilac_1},{ilac_2},{ilac_3}-->> bu ilaclar hastanızın nabız değerini düsürmekteedir"
    response = requests.post(url="https://api.telegram.org/bot5622134571:AAGCLYvoNgjNJez1gut4oNgRFMs6EBZvw8E/sendMessage", data={"chat_id":"1018753509", "text": mesaj}).json()

def yuksek_sicaklik_ilac(ilac_1,ilac_2,ilac_3,):
    mesaj=f"{ilac_1},{ilac_2},{ilac_3}-->> bu ilaclar hastanızın ateşlenmesine neden olmaktadır"
    response = requests.post(url="https://api.telegram.org/bot5622134571:AAGCLYvoNgjNJez1gut4oNgRFMs6EBZvw8E/sendMessage", data={"chat_id":"1018753509", "text": mesaj}).json()
