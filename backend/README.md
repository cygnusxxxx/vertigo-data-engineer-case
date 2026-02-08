## Yerel ortamda çalıştırma

### 1. Sanal ortam ve bağımlılıklar

Proje kökündeyken `backend` klasörüne geçin:

```bash
cd backend
```

Sanal ortam oluşturup etkinleştirin:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

Bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt
```

### 2. API'yi başlatma

Aynı `backend` klasöründeyken:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

- **Adres:** http://localhost:8080  
- **Swagger UI:** http://localhost:8080/docs  
- **ReDoc:** http://localhost:8080/redoc  



---

## Docker ile çalıştırma

`backend` klasöründen image oluşturup çalıştırın:

```bash
cd backend
docker build -t clans-api .
docker run -p 8080:8080 clans-api
```

API http://localhost:8080 adresinde çalışır.

---

## API uç noktaları

Tüm yanıtlar JSON formatındadır.

| Metot   | Endpoint              | Açıklama |
|--------|------------------------|----------|
| GET    | `/`                   | Sağlık kontrolü (`{"status": "ok"}`) |
| POST   | `/clans/`             | Klan oluştur. Query parametreleri: `name`, `region` |
| GET    | `/clans/`             | Tüm klanları listele |
| GET    | `/clans/search?q=...` | İsme göre ara (en az 3 karakter). Parametre: `q` |
| DELETE | `/clans/{id}`         | UUID ile klan sil |





