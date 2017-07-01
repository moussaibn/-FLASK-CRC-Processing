from flask import Flask, render_template, request
from fonctions import *
app = Flask(__name__)


@app.route('/CRC')
def CRC_index():
    return render_template("indexCRC.html.twig")


@app.route('/resultat', methods=['GET', 'POST'])
def CRC_calcul():
    if request.method == 'POST':
        message = request.form['message']
        resultat = Calculer(message)
        return render_template("resultatCRC.html.twig", crc=resultat)


if __name__ == '__main__':
    app.run(debug='true')
