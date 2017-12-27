from flask import *
from class_service.service import Service

from mlab import mlab_connect

app = Flask(__name__)
app.config['SECRET_KEY'] = "dankgkadjioesdfsdf"
mlab_connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<game>')
def search(game):
    filtered_services = Service.objects(game = game, occupied = False)
    return render_template('search.html', all_services = filtered_services)

@app.route('/admin')
def admin():
    return render_template('admin.html', services = Service.objects)

@app.route('/delete/<service_id>')
def delete(service_id):
    service = Service.objects().with_id(service_id)
    if service is None:
        return "Not Found"
    else:
        service.delete()
        return redirect(url_for('admin'))

@app.route('/info/<service_id>')
def info(service_id):
    info_service = Service.objects().with_id(service_id)
    info_game_pic = info_service.game + '.jpg'
    return render_template('info.html', info_game_pic = info_game_pic, info_service = info_service)

@app.route('/new_service', methods = ['GET', 'POST'])
def new_service():
    if request.method == 'GET':
        return render_template('new_service.html')
    elif request.method == 'POST':
        form = request.form
        account = form['account']
        password = form['password']
        game = form['game']
        price = form['price']
        contact = form['contact']

        new_service = Service(account = account,
                              password = password,
                              game = game,
                              price = price,
                              contact = contact,
                              occupied = False)
        new_service.save()
        flash("Service successfully created!")
        return redirect(url_for('new_service'))

@app.route('/edit/<service_id>', methods = ['GET', 'POST'])
def edit(service_id):
    if request.method == 'GET':
        service = Service.objects().with_id(service_id)
        return render_template('edit.html', service = service)
    elif request.method == 'POST':
        form = request.form
        account = form['account']
        password = form['password']
        game = form['game']
        price = form['price']
        contact = form['contact']
        occupied = form['occupied']

        service = Service.objects().with_id(service_id)
        service.update(set__account = account)
        service.update(set__password = password)
        service.update(set__game = game)
        service.update(set__price = price)
        service.update(set__contact = contact)
        service.update(set__occupied = bool(occupied))
        service.reload()
        flash("Service successfully edited!")
        return render_template('edit.html', service = service)

if __name__ == '__main__':
  app.run(debug=True)
