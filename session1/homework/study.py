from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/about-me')
def about_me():
    info = {
        'Name': 'Duy Nguyen',
        'Work': 'Students, Gamer',
        'School': 'Foreign Language Specialized School',
        'Hobbies': 'Football, Esports(PUBG, CSGO, LOL)',
        'Pet': 'No Pet',
        'Crush': 'Ex :<'
    }
    return render_template('about-me.html', me = info)

@app.route('/school')
def school():
    return redirect("http://techkids.vn")

if __name__ == '__main__':
  app.run(debug=True)
