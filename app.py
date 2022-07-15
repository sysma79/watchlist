from flask import Flask
from flask import url_for
from flask import Flask, render_template

app = Flask(__name__)#创建一个程序对象APP
#注册（添加装饰器）一个请求处理函数（视图函数view function）
#使用app.route()来绑定URL，这是一个装饰器
#WEB程序可以看作一堆视图函数的集合，编写不同的函数处理对应 URL 的请求
#/ 对应的是主机名后面的路径部分，完整 URL 就是 http://localhost:5000/。如果这里定义的 URL 规则是 /hello ，那么完整 URL 就是http://localhost:5000/hello 。
@app.route('/')

#@app.route('/home')
#@app.route('/index')

# def hello():
#     print('hello world')
#     return '欢迎来到佳源科技！<h1>Welcome to jiayuan tech!</h1><img src="http://www.jiayuantech.com/static/image/20210923/a0457d250b42ba3ae9fb52f2dcf143cd.jpg">'
#     #return '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{{ name }}'s Watchlist</title></head><body><h2>{{ name }}'s Watchlist</h2>{# 使用 length 过滤器获取 movies 变量的长度 #}<p>{{ movies|length }} Titles</p><ul>{% for movie in movies %} {# 迭代 movies 变量 #}<li>{{ movie.title }} - {{ movie.year }}</li> {# 等同于movie['title'] #}{% endfor %} {# 使用 endfor 标签结束 for 语句 #}</ul><footer><small>&copy; 2018 <a href="http://helloflask.com/tutorial">HelloFlask</a></small></footer></body></html>'

# @app.route('/user/<name>')
# def user_page(name):
#     return 'User: %s' % name

@app.route('/')
def index():
    return render_template('index.html',name=name,movies=movies)



'''
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
'''

'''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{{ name }}'s Watchlist</title>
</head>
<body>
<h2>{{ name }}'s Watchlist</h2>
{# 使用 length 过滤器获取 movies 变量的长度 #}
<p>{{ movies|length }} Titles</p>
<ul>
{% for movie in movies %} {# 迭代 movies 变量 #}
<li>{{ movie.title }} - {{ movie.year }}</li> {# 等同于
movie['title'] #}
{% endfor %} {# 使用 endfor 标签结束 for 语句 #}
</ul>
<footer>
<small>&copy; 2018 <a href="http://helloflask.com/tutori
al">HelloFlask</a></small>
</footer>
</body>
</html>
'''

name = 'Grey Li'
movies = [
{'title': 'My Neighbor Totoro', 'year': '1988'},
{'title': 'Dead Poets Society', 'year': '1989'},
{'title': 'A Perfect World', 'year': '1993'},
{'title': 'Leon', 'year': '1994'},
{'title': 'Mahjong', 'year': '1996'},
{'title': 'Swallowtail Butterfly', 'year': '1996'},
{'title': 'King of Comedy', 'year': '1999'},
{'title': 'Devils on the Doorstep', 'year': '1999'},
{'title': 'WALL-E', 'year': '2008'},
{'title': 'The Pork of Music', 'year': '2012'},
]

