import pymysql
import time
import random

baglanti= pymysql.connect(
    host="localhost",
    user="root",
    password="mysql.1..",
    db="digital_asistance",
)

yeni=baglanti.cursor()

sicaklik=round(random.uniform(36.0, 38.5), 2)



for i in range(10):
    deger=round(random.uniform(36.5,37.5),2)
    sorgu = "INSERT INTO `digital_asistance`.`sicaklik` (`deger`) VALUES (%s);" # nabiz değerini db ye kaydettik
    yeni.execute(sorgu, (deger))
    sorgu = "SELECT * FROM `digital_asistance`.`sicaklik` WHERE id = %s;"
    son_eklenen_id = yeni.lastrowid
    yeni.execute(sorgu, (son_eklenen_id,))
    son_kayit = yeni.fetchone()
    print("Son eklenen kayıt:", son_kayit)
    sorgu = "SELECT STDDEV(deger) FROM sicaklik;" # std değerini hesaplattık
    yeni.execute(sorgu)
    std = yeni.fetchone()       #std değerini atadık
    print("std: ",std)
    
    sayac=0
while True:
    time.sleep(0.1)  # Wait for 0.01 seconds (i.e., 1/100th of a second)
    std_2=std[-1]
    temp=    deger=round(random.uniform(36.5,37.5),2)
    temp2=deger
    if(abs((temp-deger))>std_2+2 or abs((temp-deger))>std_2+2 ):
        deger=temp2
    else:
        deger=temp
    sayac=sayac+1
    if(sayac%60==0):
        deger= round(random.uniform(35.5,40),2)

        sayac=0
    if(deger<40 and deger>37.5):
        print("-------------------------------------------------------")
    if(deger<=36 or deger>=40):
        print("*******************************************************")

    sorgu = "INSERT INTO `digital_asistance`.`sicaklik` (`deger`) VALUES (%s);" # nabiz değerini db ye kaydettik
    yeni.execute(sorgu, (deger))
    baglanti.commit()

    sorgu = "SELECT * FROM `digital_asistance`.`sicaklik` WHERE id = %s;"
    son_eklenen_id = yeni.lastrowid
    yeni.execute(sorgu, (son_eklenen_id,))

    son_kayit = yeni.fetchone()
    print("Son eklenen kayıt:", son_kayit)
    sorgu = "SELECT STDDEV(deger) FROM sicaklik;" # std değerini hesaplattık
    yeni.execute(sorgu)

    std = yeni.fetchone()       #std değerini atadık
    print("std: ",std)
    



    