import numpy as np

# -------------------------------
# 1.1 NumPy ile Matris İşlemleri
# -------------------------------

# 5x5 boyutunda rastgele (0-100) tam sayılardan matris
matris = np.random.randint(0, 101, size=(5,5))
print("Matris:\n", matris)

# Ortalama, standart sapma, varyans
print("Ortalama:", np.mean(matris))
print("Standart Sapma:", np.std(matris))
print("Varyans:", np.var(matris))

# En büyük ve en küçük değer
print("En Büyük:", np.max(matris))
print("En Küçük:", np.min(matris))

# Köşegen elemanlarının toplamı
print("Köşegen Toplamı:", np.trace(matris))


# -------------------------------
# 1.2 NumPy ile Veri Simülasyonu
# -------------------------------

# 1000 öğrencinin sınav puanlarını simüle et (normal dağılım, 0-100 arası)
puanlar = np.random.normal(loc=50, scale=15, size=1000)
puanlar = np.clip(puanlar, 0, 100)  # 0-100 aralığına sıkıştırma

# Ortalama, medyan, standart sapma
print("Ortalama:", np.mean(puanlar))
print("Medyan:", np.median(puanlar))
print("Standart Sapma:", np.std(puanlar))

# 50'den düşük alan öğrenci sayısı
print("50'den düşük not alan öğrenci sayısı:", np.sum(puanlar < 50))