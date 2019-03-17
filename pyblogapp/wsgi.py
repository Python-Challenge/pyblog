"""
WSGI config for pyblogapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyblogapp.settings')

application = get_wsgi_application()

'''
# add : https://qiita.com/waffle/items/835625c2413ff6a387c6
def application(environ, start_response):
    try:
        body = {k + ': ' + str(v) for k, v in environ.items()}
        start_response('200 OK', [('Content-type', 'text/plain')])
        return ['\n'.join(body).encode()]
    except:
        import traceback
        start_response('500 Internal Server Error', [('Content-type', 'text/plain')])
        return [traceback.format_exc().encode()]
'''
