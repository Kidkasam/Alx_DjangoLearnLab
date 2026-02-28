# Deployment Documentation: Social Media API

**Hosting Provider**: [Render](https://render.com)
**Live URL**: https://alx-djangolearnlab-ya84.onrender.com
**Repository**: https://github.com/your-username/Alx_DjangoLearnLab

---

## 1. Hosting Service Selection

**Render** was chosen as the hosting provider because:
- Free tier available for hobby projects
- Native PostgreSQL managed database
- Automatic HTTPS/SSL certificates
- Simple deployment from GitHub
- Environment variable management built in

---

## 2. Environment Configuration

The application uses `django-environ` to manage sensitive settings via environment variables. Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

Required environment variables:

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | A unique, random secret string |
| `DEBUG` | Set to `False` in production |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hostnames |
| `DATABASE_URL` | PostgreSQL connection string |
| `SECURE_SSL_REDIRECT` | `True` to force HTTPS |
| `AWS_ACCESS_KEY_ID` | AWS key (if using S3 for media) |
| `AWS_SECRET_ACCESS_KEY` | AWS secret key |
| `AWS_STORAGE_BUCKET_NAME` | S3 bucket name |

---

## 3. Dependencies

All production dependencies are listed in `requirements.txt`:

```
django>=6.0.1
djangorestframework
django-filter
django-environ
dj-database-url
psycopg2-binary
gunicorn
whitenoise
django-storages
boto3
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 4. Web Server Configuration

The app uses **Gunicorn** as the WSGI server. The `Procfile` at the repo root configures this:

```
web: gunicorn social_media_api.wsgi
```

**WhiteNoise** is used for serving static files efficiently without needing a separate Nginx instance (suitable for Render's managed environment):

```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- right after SecurityMiddleware
    ...
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

---

## 5. Static & Media Files

**Static files** are served by WhiteNoise. Collect them before deployment:
```bash
python manage.py collectstatic --noinput
```

**Media files** (user-uploaded content) are stored on **AWS S3** via `django-storages`:
```python
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME', default='')
```

---

## 6. Database

**Development**: SQLite (default fallback via `dj-database-url`)
**Production**: PostgreSQL managed by Render

```python
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{os.path.join(BASE_DIR, "db.sqlite3")}'
    )
}
```

Run migrations after deploying:
```bash
python manage.py migrate
```

---

## 7. Step-by-Step Deployment on Render

### Step 1: Push code to GitHub
```bash
git add .
git commit -m "production deployment config"
git push origin main
```

### Step 2: Create PostgreSQL database on Render
1. Log in at [render.com](https://render.com)
2. Click **New** → **PostgreSQL**
3. Name it `social-media-api-db`, select free tier
4. After creation, copy the **Internal Database URL**

### Step 3: Create a Web Service
1. Click **New** → **Web Service**
2. Connect your GitHub repo `Alx_DjangoLearnLab`
3. Configure:
   - **Name**: `social-media-api`
   - **Root Directory**: *(leave blank)*
   - **Runtime**: Python 3
   - **Build Command**:
     ```
     pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
     ```
   - **Start Command**:
     ```
     gunicorn social_media_api.wsgi
     ```

### Step 4: Set Environment Variables
In your Web Service → **Environment** tab:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Generate one at [djecrety.ir](https://djecrety.ir) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `social-media-api-xxxx.onrender.com` |
| `DATABASE_URL` | *(paste Internal Database URL from Step 2)* |
| `SECURE_SSL_REDIRECT` | `True` |

### Step 5: Deploy
Click **Deploy** — Render builds and launches the app. In ~5 minutes your app is live.

---

## 8. Security Checklist

- [x] `DEBUG = False`
- [x] `ALLOWED_HOSTS` configured for production domain
- [x] `SECRET_KEY` stored as environment variable, not hardcoded
- [x] `SECURE_BROWSER_XSS_FILTER = True`
- [x] `X_FRAME_OPTIONS = 'DENY'`
- [x] `SECURE_CONTENT_TYPE_NOSNIFF = True`
- [x] `SECURE_SSL_REDIRECT = True`
- [x] `SECURE_HSTS_SECONDS = 31536000`
- [x] `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
- [x] `SECURE_HSTS_PRELOAD = True`
- [x] `SESSION_COOKIE_SECURE = True`
- [x] `CSRF_COOKIE_SECURE = True`

---

## 9. Monitoring & Maintenance

### Logs
- View real-time logs in the Render dashboard: Service → **Logs** tab
- Django logs errors to stdout (captured by Render)

### Error Tracking (Recommended)
- Sign up at [sentry.io](https://sentry.io) (free tier)
- Install: `pip install sentry-sdk`
- Add to `settings.py`:
  ```python
  import sentry_sdk
  sentry_sdk.init(dsn="your-sentry-dsn", traces_sample_rate=1.0)
  ```

### Scheduled Maintenance
- **Weekly**: Check Render logs for recurring errors
- **Monthly**: Run `pip list --outdated` and update `requirements.txt`
- **Database Backups**: Enable in Render PostgreSQL dashboard → **Backups** tab

---

## 10. Final Testing Checklist (Post-Deployment)

After deployment, test these endpoints against the live URL:

| Test | Expected Result |
|------|----------------|
| `POST /api/accounts/register/` | Returns token + user data |
| `POST /api/accounts/login/` | Returns auth token |
| `GET /api/posts/` (with token) | Returns paginated posts list |
| `GET /api/posts/feed/` | Returns feed for authenticated user |
| `POST /api/posts/<id>/like/` | Likes post, creates notification |
| `GET /api/notifications/` | Returns user notifications |
| HTTPS redirect | `http://` redirects to `https://` |
| Admin panel `/admin/` | Django admin loads correctly |
