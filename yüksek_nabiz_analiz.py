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

  # İlk sorgu: besin_1 sütunu için tekrar sayısına göre en yüksek üç değeri al
  query = """
    SELECT b.besin_1, COUNT(*) AS tekrar_sayisi
    FROM beslenme b
    JOIN nabiz n ON b.tarih = n.tarih
    WHERE n.deger > 72
    GROUP BY b.besin_1
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
    print("Besin_1 için en yüksek tekrar sayıları:")
    for row in results:
      besin = row[0]
      analiz.append(row[0])
      tekrar_sayisi = row[1]
      analiz.append(row[1])
      print(f"Besin: {besin}, Tekrar Sayısı: {tekrar_sayisi}")

  except mysql.connector.Error as error:
    print(f"Hata: {error}")


  # İkinci sorgu: besin_2 sütunu için tekrar sayısına göre en yüksek üç değeri al
  query = """
    SELECT b.besin_2, COUNT(*) AS tekrar_sayisi
    FROM beslenme b
    JOIN nabiz n ON b.tarih = n.tarih
    WHERE n.deger > 72
    GROUP BY b.besin_2
    ORDER BY tekrar_sayisi DESC
    LIMIT 3
  """

  try:
    # Sorgu çalıştırılır
    cursor.execute(query)

    # Sonuçlar alınır
    results = cursor.fetchall()


    # Sonuçları ekrana yazdır
    print("\nBesin_2 için en yüksek tekrar sayıları:")
    for row in results:
      besin = row[0]
      analiz.append(row[0])
      tekrar_sayisi = row[1]
      analiz.append(row[1])
      print(f"Besin: {besin}, Tekrar Sayısı: {tekrar_sayisi}")

  except mysql.connector.Error as error:
    print(f"Hata: {error}")

# üçüncü sorgu: besin_3 sütunu için tekrar sayısına göre en yüksek üç değeri al
  query = """
    SELECT b.besin_3, COUNT(*) AS tekrar_sayisi
    FROM beslenme b
    JOIN nabiz n ON b.tarih = n.tarih
    WHERE n.deger > 72
    GROUP BY b.besin_3
    ORDER BY tekrar_sayisi DESC
    LIMIT 3
  """

  try:
    # Sorgu çalıştırılır
    cursor.execute(query)

    # Sonuçlar alınır
    results = cursor.fetchall()


    # Sonuçları ekrana yazdır
    print("\nBesin_3 için en yüksek tekrar sayıları:")
    for row in results:
      besin = row[0]
      analiz.append(row[0])
      tekrar_sayisi = row[1]
      analiz.append(row[1])
      print(f"Besin: {besin}, Tekrar Sayısı: {tekrar_sayisi}")
  except mysql.connector.Error as error:
    print(f"Hata: {error}")
    # dördüncü sorgu: besin_4 sütunu için tekrar sayısına göre en yüksek üç değeri al
  query = """
    SELECT b.besin_4, COUNT(*) AS tekrar_sayisi
    FROM beslenme b
    JOIN nabiz n ON b.tarih = n.tarih
    WHERE n.deger > 72
    GROUP BY b.besin_4
    ORDER BY tekrar_sayisi DESC
    LIMIT 3
  """

  try:
    # Sorgu çalıştırılır
    cursor.execute(query)

    # Sonuçlar alınır
    results = cursor.fetchall()


    # Sonuçları ekrana yazdır
    print("\nBesin_4 için en yüksek tekrar sayıları:")
    for row in results:
      besin = row[0]
      analiz.append(row[0])
      tekrar_sayisi = row[1]
      analiz.append(row[1])
      print(f"Besin: {besin}, Tekrar Sayısı: {tekrar_sayisi}")
    print(len(analiz))
  except mysql.connector.Error as error:
    print(f"Hata: {error}")

    
  # Cursor ve veritabanı bağlantısı kapatılır
  cursor.close()
  db.close()

analiz_mesaj.yüksek_nabiz(analiz[0],analiz[6],analiz[12],analiz[18])