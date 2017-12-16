from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi/<weight>/<height>')
def bmi(weight,height):
    weight = float(weight)
    height = float(height)
    bmi = weight / (height ** 2)
    if bmi < 16:
        result = "Severely underweight"
    elif bmi < 18.5:
        result = "Underweight"
    elif bmi<25:
        result = "Normal"
    elif bmi<30:
        result = "Overweight"
    else:
        result = "Obese"
    return result

@app.route('/bmi2/<weight>/<height>')
def bmi2(weight, height):
    weight = float(weight)
    height = float(height)

    bmi = weight / (height ** 2)

    return render_template('bmi.html', weight = weight, height = height, bmi = round(bmi,1))

if __name__ == '__main__':
    app.run(debug=True)
