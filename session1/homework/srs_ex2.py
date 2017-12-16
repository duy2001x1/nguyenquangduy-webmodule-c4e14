from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    items = [
        {
            'game': 'League of Legends',
            'rank': 'Challenger',
            'price': '1000/h',
            'status': 'Available',
            'game_pic': 'lol.jpg'
        },
        {
            'game': 'Couter-Strike: Global Offensive',
            'rank': 'Global Elite',
            'price': '1500/h',
            'status': 'Available',
            'game_pic': 'csgo.jpg'
        },
        {
            'game': "PLAYERUNKNOWN'S BATTLEGROUNDS",
            'rank': 'No rank',
            'price': '2000/h',
            'status': 'Available',
            'game_pic': 'pubg.jpg'
        }
    ]
    return render_template('index.html', items = items )

if __name__ == '__main__':
    app.run(debug=True)
