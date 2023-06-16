import mysql.connector
import analiz_mesaj

# Veritabanı bağlantısı
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql.1..",
  database="digital_asistance"
)

# Veritabanı bağlantısı başarılıysa
if db.is_connected():
  # Veritabanı bağlantısı üzerinden bir Cursor (imleç) oluşturulur
  cursor = db.cursor()

  # İlk sorgu: ilac_1 sütunu için tekrar sayısına göre en yüksek üç değeri al
  query = """
    SELECT b.ilac_1, COUNT(*) AS tekrar_sayisi
    FROM ilac_takibi b
    JOIN nabiz n ON b.tarih = n.tarih
    WHERE n.deger < 60
    GROUP BY b.ilac_1
    ORDER BY tekrar_sayisi DESC
    LIMIT 3
  """

  try:
    # Sorgu çalıştırılır
    cursor.execute(query)

    # Sonuçlar alınır
    results = cursor.fetchall()
    analiz=[]
    # Sonuçları ekrana yazdır
    print("ilac_1 için en yüksek tekrar sayıları:")
    for row in results:
      ilac = row[0]
      analiz.append(row[0])
      tekrar_sayisi = row[1]
      analiz.append(row[1])
      print(f"ilac: {ilac}, Tekrar Sayısı: {tekrar_sayisi}")

  except mysql.connector.Error as error:
    print(f"Hata: {error}")


  # İkinci sorgu: ilac_2 sütunu için tekrar sayısına göre en yüksek üç değeri al
  query = """
    SELECT b.ilac_2, COUNT(*) AS tekrar_sayisi
    FROM ilac_takibi b
    JOIN nabiz n ON b.tarih = n.tarih
    WHERE n.deger < 60
    GROUP BY b.ilac_2
    ORDER BY tekrar_sayisi DESC
    LIMIT 3
  """

  try:
    # Sorgu çalıştırılır
    cursor.execute(query)

    # Sonuçlar alınır
    results = cursor.fetchall()


    # Sonuçları ekrana yazdır
    print("\nilac_2 için en yüksek tekrar sayıları:")
    for row in results:
      ilac = row[0]
      analiz.append(row[0])
      tekrar_sayisi = row[1]
      analiz.append(row[1])
      print(f"ilac: {ilac}, Tekrar Sayısı: {tekrar_sayisi}")

  except mysql.connector.Error as error:
    print(f"Hata: {error}")

# üçüncü sorgu: ilac_3 sütunu için tekrar sayısına göre en yüksek üç değeri al
  query = """
    SELECT b.ilac_3, COUNT(*) AS tekrar_sayisi
    FROM ilac_takibi b
    JOIN nabiz n ON b.tarih = n.tarih
    WHERE n.deger < 60
    GROUP BY b.ilac_3
    ORDER BY tekrar_sayisi DESC
    LIMIT 3
  """

  try:
    # Sorgu çalıştırılır
    cursor.execute(query)

    # Sonuçlar alınır
    results = cursor.fetchall()


    # Sonuçları ekrana yazdır
    print("\nilac_3 için en yüksek tekrar sayıları:")
    for row in results:
      ilac = row[0]
      analiz.append(row[0])
      tekrar_sayisi = row[1]
      analiz.append(row[1])
      print(f"ilac: {ilac}, Tekrar Sayısı: {tekrar_sayisi}")
  except mysql.connector.Error as error:
    print(f"Hata: {error}")
   
    
  # Cursor ve veritabanı bağlantısı kapatılır
  cursor.close()
  db.close()

analiz_mesaj.dusuk_nabiz_ilac(analiz[0],analiz[6],analiz[12])