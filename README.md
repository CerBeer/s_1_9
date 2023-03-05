# s_1_9

Решение задачи в одну строчку: "\n".join(environ.get('QUERY_STRING').split("&"))

И еще по проверке на работоспособность:

curl -vv 127.0.0.1:8080/?a=1&a=2&b=3 - запрос отправляется напрямую к gunicorn
curl -vv 127.0.0.1/hello/?a=b - проверяем работает и проксирует ли nginx

gunicorn можно запускать командой gunicorn -c /path/to/config hello:application, но обязательно необходимо, что бы hello.py(wsgi который отвечает на запросы) был в той же папке откуда вызывается команда.
Чтобы не висла консоль можно запускать в фоновом режиме: gunicorn -b 0.0.0.0:8080 hello:app &

перезапустить gunicorn: sudo ps aux ﻿| grep gunicorn, ﻿и стопаете первый по порядку процесс, например: ﻿kill 33

git init

git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/CerBeer/s_1_9.git
git push -u origin main
git status

git commit -m "text"
git push -u origin master


rm -rf /home/box/web
git clone https://github.com/CerBeer/s_1_9.git /home/box/web
chmod a+x /home/box/web/init.sh
/home/box/web/init.sh
cd /home/box/web
sudo ./init.sh
sudo gunicorn -b 0.0.0.0:8080 hello:wsgi_application

nginx configtest
pkill nginx

def wsgi_application(environ, start_responce):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    data = environ['QUERY_STRING'].split('&')
    body = '\n'.join(data).encode('utf-8')
    start_responce(status, headers)
    return [body]


[bytes('\r\n'.join(environ['QUERY_STRING'].split('&')), encoding='utf8')]