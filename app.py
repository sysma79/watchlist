from flask import Flask
from flask import url_for

app = Flask(__name__)#创建一个程序对象APP
#注册（添加装饰器）一个请求处理函数（视图函数view function）
#使用app.route()来绑定URL，这是一个装饰器
#WEB程序可以看作一堆视图函数的集合，编写不同的函数处理对应 URL 的请求
#/ 对应的是主机名后面的路径部分，完整 URL 就是 http://localhost:5000/。如果这里定义的 URL 规则是 /hello ，那么完整 URL 就是http://localhost:5000/hello 。
@app.route('/')
@app.route('/home')
@app.route('/index')
def hello():
    return '欢迎来到佳源科技！<h1>Welcome to jiayuan tech!</h1><img src="http://www.jiayuantech.com/static/image/20210923/a0457d250b42ba3ae9fb52f2dcf143cd.jpg">'



@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name




@app.route('/test')
def test_url_for():
# 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
    print(url_for('hello')) # 输出：/
# 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli')) # 输出：/user/greyli
    print(url_for('user_page', name='peter')) # 输出：/user/peter
    print(url_for('test_url_for')) # 输出：/test
# 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL后面。
    print(url_for('test_url_for', num=2)) # 输出：/test?num=2
    return 'Test page'

###更改1
###