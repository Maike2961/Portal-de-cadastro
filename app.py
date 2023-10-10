from flask import Flask,render_template ,request ,redirect , url_for
from flask_login import logout_user
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=  "sqlite:///app.db"
db = SQLAlchemy(app)


class cadastro_monitor(db.Model):
    __tablename__="monitor"
    id = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String(100), nullable=False)
    etiqueta = db.Column(db.Integer)
    marca = db.Column(db.String(100))
    observacao = db.Column(db.String(100))
     
    def __str__(self):
        return self.id

class cadastro_impressoras(db.Model):
    __tablename__ ="impressoras"
    id =db.Column(db.Integer,primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    etiqueta = db.Column(db.String(80), nullable=False)
    nome_maquina = db.Column(db.String(100), nullable=False)
    serial = db.Column(db.String(80), nullable=False)
    observacao = db.Column(db.String(100))
    
    def __str__(self):
        return self.id

class cadastro_celulares(db.Model):
    __tablename__="celulares"
    id = db.Column(db.Integer,primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(10))
    usuarios = db.Column(db.String(100))
    serial = db.Column(db.String(100))
    imei1 =  db.Column(db.Integer)
    imei2 =  db.Column(db.Integer)
    
    def __str__(self):
        return self.id
    
class cadastro_notebook(db.Model):
    __tablename__="notebook"
    id = db.Column(db.Integer,primary_key=True)
    usuario = db.Column(db.String(80), nullable=False)
    etiqueta = db.Column(db.String(80), nullable=False)
    marca = db.Column(db.String(100), nullable=False)
    mac_address_fisico = db.Column(db.String(200), nullable=False)
    mac_address_wifi = db.Column(db.String(200), nullable=False)
    nome_maquina = db.Column(db.String(100), nullable=False)
    serial = db.Column(db.String(80), nullable=False)
    observacao = db.Column(db.String(100))
    data_limite = db.Column(db.Integer)
    data_manutencao = db.Column(db.Integer)
    
    def __str__(self):
        return self.id

class cadastro_software(db.Model):
    __tablename__ = "software"
    id = db.Column(db.Integer,primary_key=True)
    licenca = db.Column(db.String(200), nullable=False)
    data_renovacao = db.Column(db.String(100), nullable=False)
    suporte = db.Column(db.String(50), nullable=False)
    
    def __str__(self):
        return self.id
    
class cadastro_usuario(db.Model):
    __tablename__="webemail"
    id = db.Column(db.Integer ,primary_key=True)
    usuario = db.Column(db.String(120), nullable=False)
    email= db.Column(db.String(200), nullable=False)
    Senha = db.Column(db.String(200), nullable=False)
    
    def __str__(self):
        return self.id
@app.route("/usuario", methods=["POST", "GET"])
def usuarios():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        
        salvar = cadastro_usuario() 
        salvar.usuario = nome
        salvar.email = email
        salvar.Senha = senha
        db.session.add(salvar)
        db.session.commit()
        
    return render_template("usuario.html")
    

@app.route("/monitores", methods=["POST", "GET"])
def monitores():
    if request.method == "POST":
        usuario = request.form["usuario"]
        etiqueta = request.form["etiqueta"]
        marca = request.form["marca"]
        observacao = request.form["observacao"]
        
        salvar = cadastro_monitor()
        salvar.usuario = usuario
        salvar.etiqueta = etiqueta
        salvar.marca = marca
        salvar.observacao = observacao
        db.session.add(salvar)
        db.session.commit()
        
    return render_template("monitor.html")

@app.route("/impressoras", methods=["POST", "GET"])
def impressoras():
    if request.method == "POST":
        nome_maquina = request.form["maquina"]
        etiqueta = request.form["etiqueta"]
        marca = request.form["marca"]
        serial = request.form["serial"]
        observacao = request.form["observacao"]
        
        salvar = cadastro_impressoras()
        salvar.nome_maquina = nome_maquina
        salvar.etiqueta = etiqueta
        salvar.marca = marca
        salvar.serial = serial
        salvar.observacao = observacao
        db.session.add(salvar)
        db.session.commit()
    return render_template("impressoras.html")
        



@app.route("/celulares", methods=["POST", "GET"])
def celular():
    if request.method == "POST":
        marca = request.form.get("marca")
        status = request.form.get("status")
        serial = request.form.get("serial")
        usuarios = request.form.get("usuarios")
        imei1 = request.form.get("imei_1")
        imei2 = request.form.get("imei_2")
        
        salvar = cadastro_celulares()
        salvar.marca = marca
        salvar.status = status
        salvar.serial = serial
        salvar.usuarios = usuarios
        salvar.imei1 = imei1
        salvar.imei2 = imei2
        db.session.add(salvar)
        db.session.commit()
        
    cell = cadastro_celulares.query.all()
        
    return render_template("celulares.html", cell=cell)

@app.route("/notebook", methods=["POST", "GET"])
def notebook():
    if request.method == "POST":
        usuarios = request.form["usuario"]
        marca = request.form["marca"]
        mac_adress_fisico= request.form["adressfisico"]
        mac_adress_wifi= request.form["adresswifi"]
        nome_maquina = request.form["maquina"]
        serial = request.form["serial"]
        observacao = request.form["observacao"]
        data_manutencao = request.form["manutencao"]
        data_limite = request.form["limite"]
        
        salvar = cadastro_notebook()
        salvar.usuario = usuarios
        salvar.marca = marca
        salvar.mac_address_fisico = mac_adress_fisico
        salvar.mac_address_wifi = mac_adress_wifi
        salvar.nome_maquina = nome_maquina
        salvar.serial = serial
        salvar.data_manutencao = data_manutencao
        salvar.observacao = observacao
        salvar.data_limite = data_limite
        db.session.add(salvar)
        db.session.commit() 
    
    notes = cadastro_notebook.query.all()
        
    return render_template("notebook.html",notes=notes)

@app.route("/software", methods=["POST", "GET"])
def software():
    if request.method == "POST":
        licenca = request.form["licenca"]
        data_renovacao = request.form["data_renovacao"]
        suporte = request.form["suporte"]
        
        salvar = cadastro_software()
        salvar.licenca = licenca
        salvar.data_renovacao = data_renovacao
        salvar.suporte = suporte
        db.session.add(salvar)
        db.session.commit()
    
    return render_template("software.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/")
def principio():
    return redirect(url_for('home'))


@app.route('/delete/<int:id>')
def erase(id):
    data = notebook.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/notebook.html')

""" @app.route("/consulta", methods=["POST", "GET"])
def consulta():
    notes = cadastro_notebook.query.all()
    return render_template("notebook.html", notes=notes) """

@app.route("/consulta", methods=["POST", "GET"])
def consulta():
    cell = cadastro_celulares.query.all()
    return render_template("consulta.html", cell=cell)

@app.route("/loggout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, port=8500)
     