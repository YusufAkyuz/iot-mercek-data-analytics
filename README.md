# IoT Mercek Data Analytics

Bu proje, Arçelik'e ait IoT cihazlarından gelen `Mercek` log verilerini anlamlandırmak, işlemek ve analiz etmek amacıyla geliştirilmiştir. Ham veriler, cihazın davranışlarını ve durumlarını ifade eden sıkıştırılmış sayısal loglardan oluşur. Bu veriler, bir konfigürasyon dosyası (`v1_10.json`) yardımıyla anlamlı hale getirilip `CSV` formatında çıktıya dönüştürülür.

---

## 📁 Proje Yapısı

```
iot-mercek-data-analytics/
├── config/
│   └── v1_10.json              # Konfigürasyon dosyası (log anlamları)
├── data/
│   └── 1.txt                   # Cihazlardan gelen ham veri
├── output/
│   └── processed_data.csv      # Oluşan anlamlı verilerin çıktısı
├── scripts/
│   ├── test.py                 # Ana işlem kodu
│   ├── config_loader.py        # Konfigürasyon dosyasını yükler
│   └── transformer.py          # Log verilerini işler
│   └── mapper.py               # Anlamlandırma fonksiyonlarını içerir.
└── README.md                   # Bu dosya
```

---

## 🔧 Kurulum

1. **Python ortamı oluşturun** (önerilen: Python 3.8+)
2. **Gerekli kütüphaneleri yükleyin:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Kullanım

```bash
python scripts/test.py
```

Çalıştırıldığında:

* `data/1.txt` içindeki her satır okunur
* `logArrSize` kadar veri alınır
* `v1_10.json` konfigürasyonu ile anlamlandırılır
* Sonuçlar `output/processed_data.csv` dosyasına yazılır

---

## 📌 Dikkat Edilmesi Gerekenler

* Her veri satırı şu sırayla gelmelidir:

  ```
  ApplianceID;Latitude;Longitude;Timestamp;logArr verisi...
  ```
* `logArrSize` kadar `logArr` verisi dikkate alınır.
* `connState` (online/offline durumu) log içinde `"connState":{"S":"offline"}` gibi görünür.

---

## 📊 Örnek Çıktı (CSV)

| ApplianceId | Latitude | Longitude | Timestamp     | ConnState | SEND\_REASON  | ... |
| ----------- | -------- | --------- | ------------- | --------- | ------------- | --- |
| A9524651... | 39.95    | 32.63     | 1712395257395 | offline   | SERVICE\_CALL | ... |
| F9999043... | 36.77    | 29.09     | 1712395232384 | offline   | NORMAL        | ... |

---

## 📩 Geliştirici Notları

* Bozuk timestamp'ler `"not valid"` olarak hata mesajı dönecektir
* Eklenmesi gereken yeni `mapperFunc` türleri `transformer.py` içinde tanımlanabilir

---

## 📌 Lisans

Bu proje Sanayi ve Teknoloji bakanlığı | Yapay Zeka Uzmanlık Eğitimi paydaşı Arçelik şirketi tarafından verilmiştir ve değerlendirme amaçlıdır. Tüm hakları saklıdır.
