import pymysql
import time
import random
import mesaj

baglanti= pymysql.connect(
    host="localhost",
    user="root",
    password="mysql.1..",
    db="digital_asistance",
)

yeni=baglanti.cursor()




for i in range(10):
    deger=random.randint(95,99)
    sorgu = "INSERT INTO `digital_asistance`.`o2_saturasyonu` (`deger`) VALUES (%s);" # nabiz değerini db ye kaydettik
    yeni.execute(sorgu, (deger))
    sorgu = "SELECT * FROM `digital_asistance`.`o2_saturasyonu` WHERE id = %s;"
    son_eklenen_id = yeni.lastrowid
    yeni.execute(sorgu, (son_eklenen_id,))
    son_kayit = yeni.fetchone()
    print("Son eklenen kayıt:", son_kayit)
    sorgu = "SELECT STDDEV(deger) FROM o2_saturasyonu;" # std değerini hesaplattık
    yeni.execute(sorgu)
    std = yeni.fetchone()       #std değerini atadık
    print("std: ",std)
    
    sayac=0
    mesaj_sayac=0

while True:
    time.sleep(0.1)  # Wait for 0.01 seconds (i.e., 1/100th of a second)
    std_2=std[-1]   #std tupple olduğu en son değeri ikinci bir değişkene atadık
    temp=random.randint(90,99)
    temp2=deger
    if(abs((temp-deger))>std_2+1 or abs((temp-deger))>std_2+1 ):
        deger=temp2
        mesaj_sayac=0
    else:
        deger=temp
        mesaj_sayac=0
    sayac=sayac+1
    if(sayac%60==0):
        deger=random.randint(85,89)
        sayac=0
    if(deger<90 and mesaj_sayac<1):
        print(f"******************{mesaj_sayac}************************")
        mesaj.acil_cagri(deger)
        mesaj_sayac=1

    sorgu = "INSERT INTO `digital_asistance`.`o2_saturasyonu` (`deger`) VALUES (%s);" # nabiz değerini db ye kaydettik
    yeni.execute(sorgu, (deger))
    baglanti.commit()

    sorgu = "SELECT * FROM `digital_asistance`.`o2_saturasyonu` WHERE id = %s;"
    son_eklenen_id = yeni.lastrowid
    yeni.execute(sorgu, (son_eklenen_id,))

    son_kayit = yeni.fetchone()
    print("Son eklenen kayıt:", son_kayit)
    sorgu = "SELECT STDDEV(deger) FROM o2_saturasyonu;" # std değerini hesaplattık
    yeni.execute(sorgu)

    std = yeni.fetchone()       #std değerini atadık
    print("std: ",std)
    



    