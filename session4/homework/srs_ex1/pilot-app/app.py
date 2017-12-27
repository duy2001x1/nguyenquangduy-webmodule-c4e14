from flask import Flask, render_template, redirect, url_for, request, flash
from models.service import Service

from mlab import mlab_connect

app = Flask(__name__)
app.config["SECRET_KEY"] = "ejrklewafdsfsdf"
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


@app.route('/new_service', methods = ['GET', 'POST'])
def new_service():
    if request.method == 'GET':
        return render_template('new_service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        phone = form['phone']
        yob = form['yob']
        gender = form['gender']
        height = form['height']
        print(name, phone, yob, gender, height)

        new_service = Service(name = name,
                              phone = phone,
                              yob = yob,
                              gender = gender,
                              height = height,
                              occupied = False)
        new_service.save()
        flash("Service successfully created!")
        return redirect(url_for('new_service'))


@app.route('/edit/<service_id>', methods = ['GET', 'POST'])
def edit(service_id):
    if request.method == 'GET':
        service = Service.objects().with_id(service_id)
        return render_template('edit_service.html', service = service)
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        phone = form['phone']
        yob = form['yob']
        gender = form['gender']
        height = form['height']
        occupied = form['occupied']

        service = Service.objects().with_id(service_id)
        service.update(set__name = name)
        service.update(set__phone = phone)
        service.update(set__yob = yob)
        service.update(set__gender = gender)
        service.update(set__height = height)
        service.update(set__occupied = bool(occupied))
        service.reload()
        flash("Service successfully edited!")
        return render_template('edit_service.html', service = service)

if __name__ == '__main__':
  app.run(debug=True)
