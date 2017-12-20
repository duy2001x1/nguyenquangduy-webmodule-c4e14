from flask import Flask, render_template
from models.service import Service

from mlab import mlab_connect

app = Flask(__name__)
mlab_connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
    filtered_services = Service.objects(gender = gender, occupied = False)
    return render_template('search.html', all_services = filtered_services)

if __name__ == '__main__':
  app.run(debug=True)
