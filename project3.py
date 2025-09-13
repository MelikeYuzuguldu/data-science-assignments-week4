import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 3.1 Her dersin dağılımını histogram ile göster
# -------------------------------
df[["Matematik", "Fizik", "Kimya"]].hist(bins=10, figsize=(10,5))
plt.suptitle("Ders Dağılımları")
plt.show()

# -------------------------------
# 3.2 Bölümlere göre ortalamaları bar grafikte göster
# -------------------------------
bolum_ort = df.groupby("Bölüm")[["Ortalama"]].mean()
sns.barplot(x=bolum_ort.index, y="Ortalama", data=bolum_ort.reset_index())
plt.title("Bölümlere Göre Ortalama Başarı")
plt.show()