import os
from pathlib import Path
from dotenv import load_dotenv

# 1. .envファイルを読み込む
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# 環境変数から取得。なければデフォルト値を使用
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default-key-change-this-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
# 環境変数が 'True' の時だけ True になる設定
DEBUG = os.getenv('DEBUG') == 'True'

# 許可するホストの設定
# RenderのURL、localhost、127.0.0.1を許可
ALLOWED_HOSTS = [
    'testproject-49g3.onrender.com', 
    'localhost', 
    '127.0.0.1'
]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles", 
    'testApp',        # 自作アプリ
]

# デバッグモード時のみ Debug Toolbar を追加
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware", # 静的ファイル配信用
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# デバッグモード時のみ Debug Toolbar のミドルウェアを追加
if DEBUG:
    MIDDLEWARE.insert(3, 'debug_toolbar.middleware.DebugToolbarMiddleware')

ROOT_URLCONF = "project11th.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project11th.wsgi.application"

# Database (本番運用では通常PostgreSQLなどを使いますが、演習ではSQLiteを継続)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Internationalization
LANGUAGE_CODE = "ja" # 日本語設定に変更
TIME_ZONE = "Asia/Tokyo" # 日本時間に変更
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / 'staticfiles' # 本番用静的ファイル集約先

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Debug Toolbar用設定
INTERNAL_IPS = ["127.0.0.1", "::1"]

# --- セキュリティ強化設定 ---
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = os.getenv('SECURE_COOKIE') == 'True'
CSRF_COOKIE_SAMESITE = 'Lax'
