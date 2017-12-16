from flask import Flask, render_template
app = Flask(__name__)


@app.route('/') #when users access homepage
def index(): #call this function
    post_list = [
        "Hai con thằn lằn con",
        "Quá nhọ",
        "Anh muốn gì nào?",
        "Link"
    ]
    return render_template('index.html', article_title = "Một con vịt", posts = post_list)

@app.route('/blog')
def blog():
    posts = [
        {
            "content": "Hai con thằn lằn con",
            "author": "Thanh"
        },
        {
            "content": "Quá nhọ",
            "author": "Quân"
        },
        {
            "content": "Anh muốn gì nào?",
            "author": "Hương"
        },
        {
            "content": "Link",
            "author": "Tùng"
        },
    ]
    return render_template('blog.html', posts = posts)

@app.route('/hello_me')
def hello_me():
    return "Hello Duy"

@app.route('/hello')
def hello():
    return "Hello C4E"

@app.route('/sayhi/<name>')
def sayhi(name):
    return "Hello " + name

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
        # return str(int(a) + int(b))
        return str(a + b)

@app.route('/heading')
def heading():
    return "<h1>LMAO</h1>"

if __name__ == '__main__':
  app.run(debug=True)
