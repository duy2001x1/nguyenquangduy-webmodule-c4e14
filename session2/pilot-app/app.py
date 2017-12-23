from flask import Flask, render_template, redirect, url_for
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

@app.route('/admin')
def admin():
    return render_template('admin.html', services = Service.objects())

@app.route('/delete/<service_id>')
def delete(service_id):
    service = Service.objects().with_id(service_id)
    if service is None:
        return "Not Found"
    else:
        service.delete()
        return redirect(url_for('admin'))

if __name__ == '__main__':
  app.run(debug=True)
