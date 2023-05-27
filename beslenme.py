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

ilaclar=["Adalimumab ","Apixaban ","Duloksetin","Enoxaparin","Etanercept","Infliximab","Insülin glargin","Lansoprazol"
         ,"Montelukast","Montelukast","Pregabalin","Rivaroksaban","Rosuvastatin","Sitagliptin","Sofosbuvir","Tamsulosin",
         "Tenofovir","Trastuzumab","Vedolizumab","Venlafaksin","Zolpidem","-"]

corbalar=["Mercimek çorbası","Tarhana çorbası","Ezogelin çorbası","Tavuk suyu çorbası","Şehriye çorbası","Domates çorbası",
          "Yoğurt çorbası","Sebze çorbası","Mantar çorbası","Patates çorbası"]

yemekler=["Kuru fasulye","Türlü","İmam bayıldı","Pilav üstü tavuk","Tavuklu şehriye çorbası","Etli nohut","Sebzeli kuru fasulye"
          ,"Etli bamya","Etli dolma","Mercimek yemeği","Ispanak yemeği","Taze fasulye yemeği","Kabak yemeği","Karnıyarık",
          "Kuru patlıcan dolması","Zeytinyağlı enginar","Zeytinyağlı taze fasulye","Kıymalı pırasa sote","Çoban yemeği","Bamya yemeği"]

meyveler=["Elma","Muz","Portakal","Mandalina","Üzüm","Karpuz","Şeftali","Kiraz","Erik","Çilek"]

icecekler=["ayran","hoşaf","limonata","meyve suyu","maden suyu"]


zaman=0
sayac=0


while(True):
    time.sleep(0.001)  # Wait for 0.01 seconds (i.e., 1/100th of a second)

    zaman=zaman+1
    if(zaman%48==0 or zaman%78==0 or zaman%108==0):
        print("\n")
        besin_1=corbalar[random.randint(0,9)]
        besin_2=yemekler[random.randint(0,19)]
        besin_3=meyveler[random.randint(0,9)]
        besin_4=icecekler[random.randint(0,4)]
        kalori=random.randint(800,1200)
        sorgu = "INSERT INTO `digital_asistance`.`beslenme` (`besin_1`, `besin_2`,`besin_3`,`besin_4`,`kalori`) VALUES (%s, %s,%s,%s,%s);"
        yeni.execute(sorgu, (besin_1, besin_2,besin_3,besin_4,kalori))
        baglanti.commit()
        sorgu = "SELECT * FROM `digital_asistance`.`beslenme` WHERE id = %s;"
        son_eklenen_id = yeni.lastrowid
        yeni.execute(sorgu, (son_eklenen_id,))
        son_kayit = yeni.fetchone()
        print("Son eklenen kayıt:", son_kayit)
    if(zaman%48==0 or zaman%78==0 or zaman%108==0):
        ilac_1=ilaclar[random.randint(0,19)]
        doz_1=random.randint(1,2)
        ilac_2=ilaclar[random.randint(0,19)]
        doz_2=random.randint(1,2)
        ilac_3=ilaclar[random.randint(0,19)]
        doz_3=random.randint(1,2)
        sorgu = "INSERT INTO `digital_asistance`.`ilac_takibi` (`ilac_1`, `doz_1`,`ilac_2`, `doz_2`,`ilac_3`, `doz_3`) VALUES (%s, %s,%s,%s,%s,%s);"
        yeni.execute(sorgu, (ilac_1, doz_1,ilac_2,doz_2,ilac_3,doz_3))
        baglanti.commit()

        sorgu = "SELECT * FROM `digital_asistance`.`ilac_takibi` WHERE id = %s;"
        son_eklenen_id = yeni.lastrowid
        yeni.execute(sorgu, (son_eklenen_id,))
        son_kayit = yeni.fetchone()
        print("Son eklenen kayıt:", son_kayit)
    

    



