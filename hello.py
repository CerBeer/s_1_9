def wsgi_application(environ, start_responce):
    start_responce('200 OK', [('Content-Type', 'text/plain')])
    return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')), encoding='utf8')]
