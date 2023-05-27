import pymysql
import time
import random
import mesaj
from datetime import datetime


baglanti= pymysql.connect(
    host="localhost",
    user="root",
    password="mysql.1..",
    db="digital_asistance",
)

yeni=baglanti.cursor()




for i in range(10):

    deger=random.randint(60,70)

    sorgu = "INSERT INTO `digital_asistance`.`nabiz` (`deger`) VALUES (%s);" # nabiz değerini db ye kaydettik
    yeni.execute(sorgu, (deger))
    baglanti.commit()

    sorgu = "SELECT * FROM `digital_asistance`.`nabiz` WHERE id = %s;"
    son_eklenen_id = yeni.lastrowid
    yeni.execute(sorgu, (son_eklenen_id,))

    son_kayit = yeni.fetchone()
    print("Son eklenen kayıt:", son_kayit)
    sorgu = "SELECT STDDEV(deger) FROM nabiz;" # std değerini hesaplattık
    yeni.execute(sorgu)

    std = yeni.fetchone()       #std değerini atadık
    print("std: ",std)
    
    sayac=0
    
while True:

    time.sleep(0.01)  # Wait for 0.01 seconds (i.e., 1/100th of a second)
    zaman=datetime.now()
    dakika=zaman.strftime("%S")
    print(dakika)
    std_2=std[-1]
    temp=random.randint(57,73)
    temp2=deger
    if(abs((temp-deger))>std_2 or abs((temp-deger))>std_2 ):
        deger=temp2
        mesaj.acil_cagri(deger)
    else:
        deger=temp
        mesaj.acil_cagri(deger)

    sayac=sayac+1


    if(sayac%620==0):
        deger=random.randint(55,80)
        sayac=0
        mesaj.acil_cagri(deger)

        
    sorgu = "INSERT INTO `digital_asistance`.`nabiz` (`deger`) VALUES (%s);" # nabiz değerini db ye kaydettik
    yeni.execute(sorgu, (deger))
    baglanti.commit()

    sorgu = "SELECT * FROM `digital_asistance`.`nabiz` WHERE id = %s;"
    son_eklenen_id = yeni.lastrowid
    yeni.execute(sorgu, (son_eklenen_id,))
    son_kayit = yeni.fetchone()
    print("Son eklenen kayıt:", son_kayit)

    sorgu = "SELECT STDDEV(deger) FROM nabiz;" # std değerini hesaplattık
    yeni.execute(sorgu)
    std = yeni.fetchone()       #std değerini atadık
    print("std: ",std)
    



    