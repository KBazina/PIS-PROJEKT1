import os
from flask import Flask, render_template, request, redirect, session
from pony.orm import Database, Required, db_session, PrimaryKey, Optional
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='static')
db = Database()
db.bind(provider='sqlite', filename='auto_baza.sqlite', create_db=True)
app.config['STATIC_FOLDER'] = 'static'
app.config['UPLOAD_FOLDER'] = 'static/slike'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'jfif'}

class Auto(db.Entity):
    ID_auto = PrimaryKey(int, auto=True)
    vrsta = Required(str)
    model = Required(str)
    godište = Required(int)
    kilometraza = Required(int)
    motor = Required(str)
    snaga_motora = Required(int, column='snaga motora')
    kubikaza = Required(int)
    cijena = Required(float)
    slika = Optional(str)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def save_uploaded_file(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return filename
    else:
        return 'default_car.jpg'

db.generate_mapping(create_tables=True)

@app.route('/')
@db_session
def index():
    automobili = Auto.select()
    return render_template('index.html', automobili=automobili)

@app.route('/dodaj_auto', methods=['POST'])
@db_session
def dodaj_auto():
    marka = request.form['marka']
    model = request.form['model']
    godište = int(request.form['godište'])
    kilometraza = int(request.form['kilometraza'])
    motor = request.form['motor']
    snaga_motora = int(request.form['snaga_motora'])
    kubikaza = int(request.form['kubikaza'])
    cijena = float(request.form['cijena'])

    file = request.files['slika']
    slika = save_uploaded_file(file)

    auto = Auto(vrsta=marka, model=model,godište=godište, kilometraza=kilometraza, motor=motor,
                snaga_motora=snaga_motora, kubikaza=kubikaza, cijena=cijena,
                slika=slika)
    db.commit()

    return redirect('/')

@app.route('/obrisi_auto/<int:auto_id>', methods=['POST', 'GET'])
@db_session
def obrisi_auto(auto_id):
    auto = Auto.get(ID_auto=auto_id)
    auto.delete()
    return redirect('/')


@app.route('/uredi_auto/<int:auto_id>', methods=['GET', 'POST'])
@db_session
def uredi_auto(auto_id):
    auto = Auto.get(ID_auto=auto_id)

    if request.method == 'POST':
        kilometraza = int(request.form['kilometraza'])
        cijena = float(request.form['cijena'])
        auto.kilometraza = kilometraza
        auto.cijena = cijena
        db.commit()
        return redirect('/')

    return render_template('index.html', automobili=Auto.select())




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int("5000"),)
