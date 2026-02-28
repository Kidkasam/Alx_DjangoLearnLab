# Social Media API — Deployment Guide

A robust Social Media API built with Django REST Framework, deployed to production on **Render**.

## 🌐 Live URL

> **https://alx-djangolearnlab-ya84.onrender.com**

---

## 📦 Tech Stack

- **Backend**: Django 6 + Django REST Framework
- **Database**: PostgreSQL (via Render managed DB / `dj-database-url`)
- **Static Files**: WhiteNoise
- **Media Files**: AWS S3 (via `django-storages`)
- **Web Server**: Gunicorn
- **Hosting**: Render

---

## 🚀 Deployment Steps (Render)

### Prerequisites
- Python 3.x
- A [Render](https://render.com) account
- A GitHub account with this repo pushed

### 1. Push to GitHub
```bash
git add .
git commit -m "prepare for production deployment"
git push origin main
```

### 2. Create a Render Web Service
1. Go to [https://render.com](https://render.com) → **New** → **Web Service**
2. Connect your GitHub repo `Alx_DjangoLearnLab`
3. Set:
   - **Root Directory**: *(leave blank — Procfile is at repo root)*
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command**: `gunicorn social_media_api.wsgi`
   - **Environment**: `Python`

### 3. Create a PostgreSQL Database on Render
1. Go to **New** → **PostgreSQL**
2. After creation, copy the **Internal Database URL**

### 4. Set Environment Variables on Render
In your Web Service → **Environment** tab, add:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | A long random string |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-app-name.onrender.com` |
| `DATABASE_URL` | *(paste your PostgreSQL Internal URL)* |
| `SECURE_SSL_REDIRECT` | `True` |

### 5. Deploy
Click **Deploy** — Render will build and launch your app automatically.

---

## 🔧 Local Development Setup

```bash
# 1. Clone the repo
git clone https://github.com/your-username/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env with your local values

# 5. Run migrations
python manage.py migrate

# 6. Start server
python manage.py runserver
```

---

## 📡 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/accounts/register/` | Register a new user, returns token |
| POST | `/api/accounts/login/` | Login, returns token |
| GET/PUT | `/api/accounts/profile/` | View/update own profile |
| POST | `/api/accounts/follow/<id>/` | Follow a user |
| POST | `/api/accounts/unfollow/<id>/` | Unfollow a user |

### Posts & Comments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/posts/` | List all posts / create a post |
| GET/PUT/DELETE | `/api/posts/<id>/` | Retrieve, update, or delete a post |
| GET | `/api/posts/feed/` | Posts from users you follow |
| POST | `/api/posts/<id>/like/` | Like a post |
| POST | `/api/posts/<id>/unlike/` | Unlike a post |
| GET/POST | `/api/comments/` | List all / create a comment |
| GET/PUT/DELETE | `/api/comments/<id>/` | Retrieve, update, or delete a comment |

### Notifications
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/notifications/` | Fetch all notifications for logged-in user |

---

## 🔒 Security Configuration

The following production security settings are enabled in `settings.py`:

- `DEBUG = False`
- `SECURE_BROWSER_XSS_FILTER = True`
- `SECURE_CONTENT_TYPE_NOSNIFF = True`
- `SECURE_SSL_REDIRECT = True`
- `SECURE_HSTS_SECONDS = 31536000` (1 year)
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
- `SECURE_HSTS_PRELOAD = True`
- `SESSION_COOKIE_SECURE = True`
- `CSRF_COOKIE_SECURE = True`
- `X_FRAME_OPTIONS = 'DENY'`

---

## 📊 Monitoring & Maintenance

- **Logs**: View real-time logs in the Render dashboard under your service → **Logs** tab
- **Error Tracking**: Integrate [Sentry](https://sentry.io) for production error alerts
- **Dependency Updates**: Run `pip list --outdated` regularly and update `requirements.txt`
- **Database Backups**: Enable automatic backups in the Render PostgreSQL dashboard

---

## ✅ Deployment Checklist

- [x] `DEBUG = False`
- [x] `ALLOWED_HOSTS` configured
- [x] `SECRET_KEY` stored in environment variable (not hardcoded)
- [x] Security headers enabled
- [x] HTTPS redirection enabled (`SECURE_SSL_REDIRECT`)
- [x] Static files served via WhiteNoise
- [x] Database configured via `DATABASE_URL`
- [x] `Procfile` configured for Gunicorn
- [x] `requirements.txt` includes all production dependencies
- [ ] Live URL confirmed and working
