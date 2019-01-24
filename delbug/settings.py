"""
Django settings for delbug project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*d-sm(p7fl%$7d8lazz3nf8!+hg^6+2d*=yzem-hcj#9htwc#o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bug',
    'bootstrap3',
    # 'tinymce',
    # 'ckeditor',
    # 'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'delbug.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'delbug.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'NAME': 'delbug',
        'USER': 'root',
        'PASSWORD': 'password',
        'OPTIONS': {
            # 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'init_command': "SET sql_mode='traditional'",
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'bug/static'),
]

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'delbug/../bug/templates'),)

# TINYMCE_DEFAULT_CONFIG = {
#     'theme': 'advanced',
#     'width': 600,
#     'height': 400,
# }
#
# # ckeditor config
# CKEDITOR_UPLOAD_PATH = 'article_files/'
# CKEDITOR_JQUERY_URL ='js/jquery-3.2.1.min.js'
# CKEDITOR_IMAGE_BACKEND = 'pillow'
# CKEDITOR_CONFIGS = {
#     'default': {
#         'language': 'zh-cn',
#         'toolbar_YourCustomToolbarConfig': [
#
#             {'name': 'clipboard', 'items': ['Undo', 'Redo', '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord']},
#             {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote']},
#             {'name': 'insert', 'items': ['Image', 'Table', 'HorizontalRule', 'Smiley']},
#             {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
#             {'name': 'editing', 'items': ['Find', 'Replace', '-']},
#             {'name': 'tools', 'items': ['Maximize']},
#             '/',
#             {'name': 'styles', 'items': ['Format', 'Font', 'FontSize']},
#             {'name': 'basicstyles',
#              'items': ['Bold', 'Italic', 'Underline', 'Strike', '-', 'RemoveFormat']},
#             {'name': 'colors', 'items': ['TextColor', 'BGColor']},
#             {'name': 'paragraph',
#              'items': ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
#             {'name': 'document', 'items': ['Source']},
#         ],
#         'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
#         'width': '100%',
#         'tabSpaces': 4,
#         'extraPlugins': ','.join([
#             'uploadimage',  # the upload image feature
#             # your extra plugins here
#             'div',
#             'autolink',
#             'autoembed',
#             'embedsemantic',
#             'autogrow',
#             'widget',
#             'lineutils',
#             'clipboard',
#             'dialog',
#             'dialogui',
#             'elementspath'
#         ]),
#     }
# }
# CKEDITOR_ALLOW_NONIMAGE_FILES = False
# CKEDITOR_BROWSE_SHOW_DIRS = True
#
# # media_confige
# MEDIA_URL = 'media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'bug/media')