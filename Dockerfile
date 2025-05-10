# BAse image tanımı
FROM python:3.10-slim

WORKDIR /app

# Gereken dosyaları kopyala
COPY scripts/ scripts/
COPY config/ config/
COPY data/ data/
COPY requirements.txt .

# Python bağımlılıklarını yükle
RUN pip install --no-cache-dir -r requirements.txt

# Çıktı klasörünü outpt olarak oluşturur
RUN mkdir -p output

# Main script dosyasını çalıştırır
CMD ["python", "scripts/test.py"]
