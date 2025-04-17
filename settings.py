import os

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Ajoutez ceci pour éviter des problèmes de sécurité sur Render
if 'RENDER' in os.environ:
    ALLOWED_HOSTS.append(os.environ['RENDER_EXTERNAL_HOSTNAME'])
    DEBUG = False
else:
    ALLOWED_HOSTS = []
    DEBUG = True
