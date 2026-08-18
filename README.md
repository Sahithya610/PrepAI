# PrepAI — AI-Powered Interview Preparation Platform

> A production-ready REST API that helps developers prepare for
> technical interviews with AI-generated feedback and scoring.

## 🌐 Live Demo

- **API Base URL**: https://prepai-api-aobf.onrender.com
- **Interactive Docs**: https://prepai-api-aobf.onrender.com/docs

## ✨ Features

- 🔐 Secure user authentication with JWT tokens
- 📝 Create and manage interview practice sessions by role and difficulty
- ❓ Add interview questions to each session
- 🤖 Get AI-generated feedback and scores (1-10) on your answers
- 📊 Track improvement across multiple sessions
- 🛡️ Full data isolation — users can only access their own data

## 🛠️ Tech Stack

| Layer          | Technology           |
| -------------- | -------------------- |
| Framework      | FastAPI              |
| Database       | PostgreSQL 17        |
| ORM            | SQLAlchemy + Alembic |
| Authentication | JWT + bcrypt         |
| AI Feedback    | Groq LLaMA 3.1       |
| Deployment     | Render               |
| Testing        | Pytest               |

## 📡 API Endpoints

### Auth

| Method | Endpoint       | Description    |
| ------ | -------------- | -------------- |
| POST   | /auth/register | Create account |
| POST   | /auth/login    | Get JWT token  |

### Users

| Method | Endpoint  | Description    |
| ------ | --------- | -------------- |
| GET    | /users/me | Get profile    |
| PUT    | /users/me | Update profile |

### Sessions

| Method | Endpoint       | Description    |
| ------ | -------------- | -------------- |
| POST   | /sessions/     | Create session |
| GET    | /sessions/     | List sessions  |
| GET    | /sessions/{id} | Get session    |
| PUT    | /sessions/{id} | Update session |
| DELETE | /sessions/{id} | Delete session |

### Questions

| Method | Endpoint                 | Description     |
| ------ | ------------------------ | --------------- |
| POST   | /sessions/{id}/questions | Add question    |
| PATCH  | /sessions/{id}/answer    | Submit answer   |
| POST   | /sessions/{id}/feedback  | Get AI feedback |

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL
- Groq API key (free at console.groq.com)

### Local Setup

```bash
# Clone repo
git clone https://github.com/Sahithya610/PrepAI
cd PrepAI

# Setup environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your values

# Run migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

### Visit

- API: http://localhost:8000
- Docs: http://localhost:8000/docs

## 🧪 Testing

```bash
pytest tests/ -v
```

## 👤 Author

**Sahithya**  
[GitHub](https://github.com/Sahithya610)
