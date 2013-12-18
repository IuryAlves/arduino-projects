from flask import app, request, Flask, render_template, request, url_for
import serial
import os

ser = serial.Serial("/dev/ttyACM0", 9600)
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template')
app = Flask(__name__, template_folder=tmpl_dir)
app.config.from_object(__name__)


@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")


@app.route("/cadastro", methods=["GET","POST"])
def cadastro():
    if request.method == "POST":
        dado = request.form["msg"]
        for char in str(dado):
            ser.write(char)
    return render_template('cadastro.html')


if __name__ == '__main__':
     app.run(host='0.0.0.0') #para rodar nao localmente
    #app.debug = True
    #app.run()
