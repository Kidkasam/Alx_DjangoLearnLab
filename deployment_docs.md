# Deployment Documentation: Social Media API

This document provides instructions for deploying the Social Media API to a production environment (e.g., Heroku, AWS, DigitalOcean).

## 1. Environment Configuration

The application uses `django-environ` to manage sensitive settings. Create a `.env` file in the root directory (refer to `.env.example`) and set the following variables:

- `SECRET_KEY`: A unique, secret string for cryptographic signing.
- `DEBUG`: Set to `False` in production.
- `ALLOWED_HOSTS`: A comma-separated list of host/domain names that this Django site can serve.
- `DATABASE_URL`: Connection string for your production database (e.g., PostgreSQL).
- `SECURE_SSL_REDIRECT`: Set to `True` if using HTTPS.

## 2. Dependencies

Install the production dependencies using:

```bash
pip install -r requirements.txt
```

## 3. Static Files

The app uses `WhiteNoise` to serve static files. To collect static files for production, run:

```bash
python manage.py collectstatic --noinput
```

## 4. Database Migrations

Apply database migrations:

```bash
python manage.py migrate
```

## 5. Web Server

In production, use a WSGI server like `Gunicorn`. The `Procfile` is configured for this:

```bash
# Example command to run locally with Gunicorn
gunicorn social_media_api.wsgi
```

## 6. Security Checklist

- [x] `DEBUG` is `False`.
- [x] `ALLOWED_HOSTS` is configured.
- [x] `SECRET_KEY` is kept private.
- [x] Security headers are enabled (`SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, etc.).
- [x] HTTPS redirection is enabled (`SECURE_SSL_REDIRECT`).

## 7. Monitoring

- Monitor application logs for errors.
- Use tools like Sentry for error tracking or New Relic for performance monitoring.
