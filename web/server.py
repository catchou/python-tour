#负责启动wsgi服务器
#从wsgiref模块导入
from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 9999, application)
print('Serving HTTP on port 9999...')
httpd.serve_forever()
