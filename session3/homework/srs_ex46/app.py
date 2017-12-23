from flask import Flask, render_template, redirect, url_for
from class_service.service import Service

from mlab import mlab_connect

app = Flask(__name__)
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
    info_account = info_service.account
    info_password = info_service.password
    info_game = info_service.game
    info_price = info_service.price
    info_contact = info_service.contact
    return render_template('info.html', info_game_pic = info_game_pic,
                                        info_account = info_account,
                                        info_password = info_password,
                                        info_game = info_game,
                                        info_price = info_price,
                                        info_contact = info_contact)

if __name__ == '__main__':
  app.run(debug=True)
