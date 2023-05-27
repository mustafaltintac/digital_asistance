import pymysql
import random
import time

baglanti=pymysql.connect(
    host="localhost",
    user="root",
    password="mysql.1..",
    db="digital_asistance",
)

yeni=baglanti.cursor()

durumlar=["çok iyi","iyi","normal","kötü","çok kötü"]
belirtiler=["göğüs ağrısı","nefes darlığı","mide bulantısı","baş dönmesi","yorgunluk","baş ağrısı","bulanık görme",
            "kulak çınlaması","hızlı nefes alma","çarpıntı veya hızlı kalp atışı","soğuk eller ve ayaklar","şiddetli ağrı",
            "sıcaklık artışı","şişlik","konuşma veya görme bozukluğu","nefes darlığı  veya nefes almada güçlük","öksürük ve göğüs ağrısı",
            "yorgunluk veya halsizlik","ödem","idrar yaparken zorlanma","hırıltılı solunum","göğüs sıkışması","uyku problem,",
            "kronik ökdürük","balgam üretimi","ses kısıklığı","iştah kaybı","titreme","titreme-terleme","halszilik","hafıza sorunları",
            "solunum yavaşlaması","ciltte soluluk","sıcak basması","yoğun terleme","kalp artışlarında hızlanma",]


zaman=0

while(True):
    time.sleep(0.1)  # Wait for 0.01 seconds (i.e., 1/100th of a second)

    zaman=zaman+1
    if(zaman%360==0 or zaman%720==0 or zaman%1080==0 or 1440):
        print("\n")
        if(durumlar[random.randint(0,4)]=="çok iyi"):
            hastanin_durumu="çok iyi"
            belirti_1="-"
            belirti_2="-"
            belirti_3="-"
            belirti_4="-"
            belirti_5="-"
            sorgu = "INSERT INTO `digital_asistance`.`hasta_durum_takibi` (`hastanin_durumu`, `belirti_1`,`belirti_2`, `belirti_3`,`belirti_4`, `belirti_5`) VALUES (%s, %s,%s,%s,%s,%s);"
            yeni.execute(sorgu, (hastanin_durumu, belirti_1,belirti_2,belirti_3,belirti_4,belirti_5))
            baglanti.commit()
            sorgu = "SELECT * FROM `digital_asistance`.`hasta_durum_takibi` WHERE id = %s;"
            son_eklenen_id = yeni.lastrowid
            yeni.execute(sorgu, (son_eklenen_id,))
            son_kayit = yeni.fetchone()
            print("Son eklenen kayıt:", son_kayit)

        elif(durumlar[random.randint(0,4)]=="iyi"):
            hastanin_durumu="iyi"
            belirti_1=belirtiler[random.randint(0,35)]
            belirti_2="-"
            belirti_3="-"
            belirti_4="-"
            belirti_5="-"
            sorgu = "INSERT INTO `digital_asistance`.`hasta_durum_takibi` (`hastanin_durumu`, `belirti_1`,`belirti_2`, `belirti_3`,`belirti_4`, `belirti_5`) VALUES (%s, %s,%s,%s,%s,%s);"
            yeni.execute(sorgu, (hastanin_durumu, belirti_1,belirti_2,belirti_3,belirti_4,belirti_5))
            baglanti.commit()
            sorgu = "SELECT * FROM `digital_asistance`.`hasta_durum_takibi` WHERE id = %s;"
            son_eklenen_id = yeni.lastrowid
            yeni.execute(sorgu, (son_eklenen_id,))
            son_kayit = yeni.fetchone()
            print("Son eklenen kayıt:", son_kayit)
        elif(durumlar[random.randint(0,4)]=="normal"):
            hastanin_durumu="normal"
            belirti_1=belirtiler[random.randint(0,35)]
            belirti_2=belirtiler[random.randint(0,35)]
            belirti_3="-"
            belirti_4="-"
            belirti_5="-"
            sorgu = "INSERT INTO `digital_asistance`.`hasta_durum_takibi` (`hastanin_durumu`, `belirti_1`,`belirti_2`, `belirti_3`,`belirti_4`, `belirti_5`) VALUES (%s, %s,%s,%s,%s,%s);"
            yeni.execute(sorgu, (hastanin_durumu, belirti_1,belirti_2,belirti_3,belirti_4,belirti_5))
            baglanti.commit()
            sorgu = "SELECT * FROM `digital_asistance`.`hasta_durum_takibi` WHERE id = %s;"
            son_eklenen_id = yeni.lastrowid
            yeni.execute(sorgu, (son_eklenen_id,))
            son_kayit = yeni.fetchone()
            print("Son eklenen kayıt:", son_kayit)
        elif(durumlar[random.randint(0,4)]=="kötü"):
            hastanin_durumu="kötü"
            belirti_1=belirtiler[random.randint(0,35)]
            belirti_2=belirtiler[random.randint(0,35)]
            belirti_3=belirtiler[random.randint(0,35)]
            belirti_4="-"
            belirti_5="-"
            sorgu = "INSERT INTO `digital_asistance`.`hasta_durum_takibi` (`hastanin_durumu`, `belirti_1`,`belirti_2`, `belirti_3`,`belirti_4`, `belirti_5`) VALUES (%s, %s,%s,%s,%s,%s);"
            yeni.execute(sorgu, (hastanin_durumu, belirti_1,belirti_2,belirti_3,belirti_4,belirti_5))
            baglanti.commit()
            sorgu = "SELECT * FROM `digital_asistance`.`hasta_durum_takibi` WHERE id = %s;"
            son_eklenen_id = yeni.lastrowid
            yeni.execute(sorgu, (son_eklenen_id,))
            son_kayit = yeni.fetchone()
            print("Son eklenen kayıt:", son_kayit)
        else:
            hastanin_durumu="çok kötü"
            belirti_1=belirtiler[random.randint(0,35)]
            belirti_2=belirtiler[random.randint(0,35)]
            belirti_3=belirtiler[random.randint(0,35)]
            belirti_4=belirtiler[random.randint(0,35)]
            belirti_5=belirtiler[random.randint(0,35)]
            sorgu = "INSERT INTO `digital_asistance`.`hasta_durum_takibi` (`hastanin_durumu`, `belirti_1`,`belirti_2`, `belirti_3`,`belirti_4`, `belirti_5`) VALUES (%s, %s,%s,%s,%s,%s);"
            yeni.execute(sorgu, (hastanin_durumu, belirti_1,belirti_2,belirti_3,belirti_4,belirti_5))
            baglanti.commit()
            sorgu = "SELECT * FROM `digital_asistance`.`hasta_durum_takibi` WHERE id = %s;"
            son_eklenen_id = yeni.lastrowid
            yeni.execute(sorgu, (son_eklenen_id,))
            son_kayit = yeni.fetchone()
            print("Son eklenen kayıt:", son_kayit)
            
