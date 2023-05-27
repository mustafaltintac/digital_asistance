import pymysql


baglanti=pymysql.connect(
    host="localhost",
    user="root",
    password="mysql.1..",
    db="digital_asistance",
    
)

yeni=baglanti.cursor()

ilaclar=["Adalimumab ","Apixaban ","Duloksetin","Enoxaparin","Etanercept","Infliximab","Insülin glargin","Lansoprazol"
         ,"Montelukast","Pregabalin","Rivaroksaban","Rosuvastatin","Sitagliptin","Sofosbuvir","Tamsulosin",
         "Tenofovir","Trastuzumab","Vedolizumab","Venlafaksin","Zolpidem"]

corbalar=["Mercimek çorbası","Tarhana çorbası","Ezogelin çorbası","Tavuk suyu çorbası","Şehriye çorbası","Domates çorbası",
          "Yoğurt çorbası","Sebze çorbası","Mantar çorbası","Patates çorbası"]

yemekler=["Kuru fasulye","Türlü","İmam bayıldı","Pilav üstü tavuk","Tavuklu şehriye çorbası","Etli nohut","Sebzeli kuru fasulye"
          ,"Etli bamya","Etli dolma","Mercimek yemeği","Ispanak yemeği","Taze fasulye yemeği","Kabak yemeği","Karnıyarık",
          "Kuru patlıcan dolması","Zeytinyağlı enginar","Zeytinyağlı taze fasulye","Kıymalı pırasa sote","Çoban yemeği","Bamya yemeği"]

meyveler=["Elma","Muz","Portakal","Mandalina","Üzüm","Karpuz","Şeftali","Kiraz","Erik","Çilek"]

icecekler=["ayran","hoşaf","limonata","meyve suyu","maden suyu"]

hashYemekler=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hashCorbalar=[0,0,0,0,0,0,0,0,0,0]
hashMeyveler=[0,0,0,0,0,0,0,0,0,0]
hashIcecekler=[0,0,0,0,0]
hashIlaclar=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

sorgu="SELECT MIN(id) FROM beslenme;"
yeni.execute(sorgu)
sonuc = yeni.fetchone()
baslangic=sonuc[0]
print("İlk kaydın ID'si:", baslangic)

sorgu="SELECT Max(id) FROM beslenme;"
yeni.execute(sorgu)
sonuc = yeni.fetchone()
bitis=sonuc[0]
print("İlk kaydın ID'si:", bitis)

sorgu="SELECT besin_1,besin_2,besin_3,besin_4 FROM beslenme;"
yeni.execute(sorgu) 
sonuc = yeni.fetchall()
print("İlk kaydın ID'si:", sonuc[0])
print(sonuc[1][0])
print(sonuc[0][1])
print(sonuc[0][2])
print(sonuc[0][3])
for i in range(bitis-baslangic):
    if sonuc[i][0] in corbalar:
        index = corbalar.index(sonuc[i][0])
        hashCorbalar[index]+=1
    if sonuc[i][1] in yemekler:
        index = yemekler.index(sonuc[i][1])
        hashYemekler[index]+=1            
    if sonuc[i][2] in meyveler:
        index = meyveler.index(sonuc[i][2])
        hashMeyveler[index]+=1
    if sonuc[i][3] in icecekler:
        index = icecekler.index(sonuc[i][3])
        hashIcecekler[index]+=1

print(hashCorbalar,hashYemekler,hashMeyveler,hashIcecekler)

en_buyuk_1 = hashCorbalar.index(max(hashCorbalar))
print(corbalar[en_buyuk_1],en_buyuk_1)
hashCorbalar.pop(en_buyuk_1)

en_buyuk_2 = hashCorbalar.index(max(hashCorbalar))
print(corbalar[en_buyuk_2+1],en_buyuk_2+1)
hashCorbalar.pop(en_buyuk_2)

en_buyuk_3 = hashCorbalar.index(max(hashCorbalar))
print(corbalar[en_buyuk_3+2],en_buyuk_3+2)
hashCorbalar.pop(en_buyuk_3)

en_buyuk_1 = hashYemekler.index(max(hashYemekler))
print(yemekler[en_buyuk_1],en_buyuk_1)
hashYemekler.pop(en_buyuk_1)

en_buyuk_2 = hashCorbalar.index(max(hashCorbalar))
print(yemekler[en_buyuk_2+1],en_buyuk_2+1)
hashYemekler.pop(en_buyuk_2)

en_buyuk_3 = hashYemekler.index(max(hashYemekler))
print(yemekler[en_buyuk_3+2],en_buyuk_3+2)
hashYemekler.pop(en_buyuk_3)

en_buyuk_1 = hashMeyveler.index(max(hashMeyveler))
print(meyveler[en_buyuk_1],en_buyuk_1)
hashMeyveler.pop(en_buyuk_1)

en_buyuk_2 = hashMeyveler.index(max(hashMeyveler))
print(meyveler[en_buyuk_2+1],en_buyuk_2+1)
hashMeyveler.pop(en_buyuk_2)

en_buyuk_3 = hashMeyveler.index(max(hashMeyveler))
print(meyveler[en_buyuk_3+2],en_buyuk_3+2)
hashMeyveler.pop(en_buyuk_3)


en_buyuk_1 = hashIcecekler.index(max(hashIcecekler))
print(icecekler[en_buyuk_1],en_buyuk_1)
hashMeyveler.pop(en_buyuk_1)

en_buyuk_2 = hashIcecekler.index(max(hashIcecekler))
print(icecekler[en_buyuk_2+1],en_buyuk_2+1)
hashIcecekler.pop(en_buyuk_2)

en_buyuk_3 = hashIcecekler.index(max(hashIcecekler))
print(icecekler[en_buyuk_3+2],en_buyuk_3+2)
hashIcecekler.pop(en_buyuk_3)



