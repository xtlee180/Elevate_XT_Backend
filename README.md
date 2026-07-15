# Elevate_XT Backend

The **Elevate_XT Backend** is a modular, scalable FastAPI application powering the Elevate.XT developer‑growth platform.  
It provides authentication, user management, AI‑powered features, and a clean architecture designed for long‑term expansion.

---

## 🚀 Features

### 🔐 Authentication
- JWT‑based login system
- Secure password hashing (Argon2)
- Protected `/auth/me` endpoint
- Token verification + user extraction

### 👤 User System
- User model (SQLAlchemy)
- User schemas (Pydantic)
- User service layer
- User router (API v1)

### 🧠 AI Integration (coming soon)
- AI project generator
- AI task generator
- AI hints & explanations
- AI readiness scoring

### 📦 Modular Architecture
- Routers (`app/api/v1`)
- Services (`app/services`)
- Schemas (`app/schemas`)
- Models (`app/models`)
- Core utilities (`app/core`)
- Database session + initialization (`app/db`)

---

### 📁 Project Structure
app/
main.py
api/
v1/
auth_router.py
users.py
core/
security.py
db/
session.py
init_db.py
models/
user.py
schemas/
auth.py
user.py
services/
auth_service.py
user_service.py
utils/


This structure follows industry‑standard FastAPI architecture with clear separation of concerns.

---

### 🛠️ Tech Stack
- **Python 3.10+**
- **FastAPI**
- **SQLAlchemy**
- **Pydantic**
- **Argon2 password hashing**
- **JWT authentication**
- **PostgreSQL** (via EDB or standard Postgres)
- **Uvicorn** (development server)

---

### 🔧 Installation

### 1. Clone the repository
git clone https://github.com/xtlee180/Elevate_XT_Backend.git
cd Elevate_XT_Backend

### 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

### 3. Install dependencies
pip install -r requirements.txt

### ⚙️ Environment Variables
Create a .env file in the project root:
DATABASE_URL=postgresql://user:password@localhost:5432/elevate_xt
SECRET_KEY=your-secret-key

⚠️ Important: .env is ignored by Git and should never be committed.

### ▶️ Running the Backend
Start the FastAPI server:
uvicorn app.main:app --reload

API docs available at:
- Swagger UI → http://localhost:8000/docs
- ReDoc → http://localhost:8000/redoc

### 🔐 Authentication Endpoints
POST /auth/login
Login with email + password
Returns JWT access token.

GET /auth/me
Protected route
Requires Authorization: Bearer <token>  
Returns current user info.

---
### 📌 Roadmap
[ ] Projects API (CRUD)
[ ] Tasks API (CRUD + progress tracking)
[ ] AI project generator
[ ] AI task generator
[ ] Dashboard analytics
[ ] User roles (admin, mentor, student)
[ ] Docker deployment
[ ] CI/CD with GitHub Actions

---

### 🧑‍💻 Author
Xian‑Ting Lee  
Creator of Elevate.XT — an AI‑powered developer growth platform.

---

### ⭐ License
MIT License
Feel free to use, modify, and contribute.

---
If you want, I can also generate:

- a **requirements.txt**  
- a **LICENSE file**  
- a **CONTRIBUTING.md**  
- a **project logo** (AI‑generated)  
- a **GitHub Actions CI/CD workflow**  
- a **Dockerfile + docker‑compose.yml**

Just tell me what you want next.
