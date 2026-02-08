## Running in a local environment

### 1. Virtual environment and dependencies

While in the project root, navigate to the backend folder:


```bash
cd backend
```

Create and activate the virtual environment:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Starting the API

While in the same backend folder:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

- **Address:** http://localhost:8080  
- **Swagger UI:** http://localhost:8080/docs  
- **ReDoc:** http://localhost:8080/redoc  



---

## Running with Docker
Create and run the image from the backend folder:
 

```bash
cd backend
docker build -t clans-api .
docker run -p 8080:8080 clans-api
```

API http://localhost:8080 adresinde çalışır.

---

## API endpoints
All responses are in JSON format.

| Method   | Endpoint              | Description |
|--------|------------------------|----------|
| GET    | `/`                   | Health check (`{"status": "ok"}`) |
| POST   | `/clans/`             | Create a clan. Query parameters: `name`, `region` |
| GET    | `/clans/`             | List all clans |
| GET    | `/clans/search?q=...` | Search by name (at least 3 characters). Parameter: `q` |
| DELETE | `/clans/{id}`         | Delete clan by UUID |






