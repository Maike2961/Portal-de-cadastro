from flask import Flask,render_template ,request ,redirect , url_for, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import logout_user
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///app.db"
app.config["SECRET_KEY"] = "secreta123"

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
    __tablename__ ="software"
    id = db.Column(db.Integer,primary_key=True)
    licenca = db.Column(db.String(200), nullable=False, unique=True)
    data_renovacao = db.Column(db.String(100), nullable=False)
    suporte = db.Column(db.String(50), nullable=False)
    
    def __str__(self):
        return self.id
    
class cadastro_usuario(db.Model):
    __tablename__="usuario"
    id = db.Column(db.Integer ,primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email= db.Column(db.String(200), nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    
    def __str__(self):
        return self.id
    
    
class file(db.Model):
    __tablename__ = "file_pdf"
    id = db.Column(db.Integer, primary_key=True)
    file = db.Column(db.String(100), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    
    def __str__(self):
        return self.id
    
#cadastrar usuario
@app.route("/usuario", methods=["POST", "GET"])
def usuarios():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        
        if not nome or not email or not senha:
            flash("Por favor preencha todos os campos solicitados")
        else:
            salvar = cadastro_usuario() 
            salvar.nome = nome
            salvar.email = email
            salvar.senha = senha
            db.session.add(salvar)
            db.session.commit()
    
    usuar = cadastro_usuario.query.all()
        
    return render_template("usuario.html", usuar=usuar)
    
#cadastrar monitores
@app.route("/monitores", methods=["POST", "GET"])
def monitores():
    if request.method == "POST":
        usuario = request.form["usuario"]
        etiqueta = request.form["etiqueta"]
        marca = request.form["marca"]
        observacao = request.form["observacao"]
        
        if not usuario or not etiqueta or not marca:
            flash("Por favor preencha os campos desde usuário até marca")
        else:
            salvar = cadastro_monitor()
            salvar.usuario = usuario
            salvar.etiqueta = etiqueta
            salvar.marca = marca
            salvar.observacao = observacao
            db.session.add(salvar)
            db.session.commit()
    
    monit = cadastro_monitor.query.all()
        
    return render_template("monitor.html", monit=monit)

#cadastrar impressoras
@app.route("/impressoras", methods=["POST", "GET"])
def impressoras():
    if request.method == "POST":
        nome_maquina = request.form["maquina"]
        etiqueta = request.form["etiqueta"]
        marca = request.form["marca"]
        serial = request.form["serial"]
        observacao = request.form["observacao"]
        
        if not nome_maquina or not etiqueta or not marca or not serial:
            flash("Por favor preencha todos os campos solicitados desde maquina até serial")
        else:
            salvar = cadastro_impressoras()
            salvar.nome_maquina = nome_maquina
            salvar.etiqueta = etiqueta
            salvar.marca = marca
            salvar.serial = serial
            salvar.observacao = observacao
            db.session.add(salvar)
            db.session.commit()
        
    impressor = cadastro_impressoras.query.all()
    return render_template("impressoras.html", impressor=impressor)
        
#cadastrar celulares
@app.route("/celulares", methods=["POST", "GET"])
def celular():
    if request.method == "POST":
        marca = request.form.get("marca")
        status = request.form.get("status")
        serial = request.form.get("serial")
        usuarios = request.form.get("usuarios")
        imei1 = request.form.get("imei_1")
        imei2 = request.form.get("imei_2")
        
        if not marca or not status or not  serial or not usuarios or not imei1:
            flash("Por favor, Preencha todos os campos")
        else:
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

#cadastrar notebook
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
        
       #banana
        x = data_limite
        y = data_manutencao
        first = datetime.strptime(x, "%Y-%m-%d").strftime("%d/%m/%Y")
        second = datetime.strptime(y, "%Y-%m-%d").strftime("%d/%m/%Y")
        
        if first < second:
            flash("data incomparaveis")
            print("datas incomparaveis")
        else:
            salvar = cadastro_notebook()
            salvar.usuario = usuarios
            salvar.marca = marca
            salvar.mac_address_fisico = mac_adress_fisico
            salvar.mac_address_wifi = mac_adress_wifi
            salvar.nome_maquina = nome_maquina
            salvar.serial = serial
            salvar.data_manutencao = second
            salvar.data_limite = first
            salvar.observacao = observacao
            db.session.add(salvar)
            db.session.commit() 
    
    notes = cadastro_notebook.query.all()
        
    return render_template("notebook.html",notes=notes)

#Cadastrar Software
@app.route("/software", methods=["POST", "GET"])
def software():
    if request.method == "POST":
        licenca = request.form["licenca"]
        data_renovacao = request.form["data_renovacao"]
        suporte = request.form["suporte"]
        
        data_renovacao2 = datetime.strptime(data_renovacao, "%Y-%m-%d").strftime("%d/%m/%Y")
        
        if not licenca or not data_renovacao or not suporte:
            flash("Por favor, preencha todos os campos")
        else:
            salvar = cadastro_software()
            salvar.licenca = licenca
            salvar.data_renovacao = data_renovacao2
            salvar.suporte = suporte
            db.session.add(salvar)
            db.session.commit()

    soft = cadastro_software.query.all()
    
    return render_template("software.html", soft=soft)

#consulta termos de responsabilidade
@app.route("/termo", methods=["GET", "POST"])
def termo():
    if request.method == "POST":
        files = request.form["file"]
        nome = request.form["nome"]
        
        if not nome or not files:
            flash("por favor preencha todos os campos antes de salvar")
        else:
            salvar = file()
            salvar.file = files
            salvar.nome = nome
            db.session.add(salvar)
            db.session.commit()
    arquivos = file.query.all()
    
    return render_template("termo.html", arquivos=arquivos)

 

#remover celular
@app.route("/remover_celular/<int:id>")
def cellremover(id):
    cell = cadastro_celulares.query.filter_by(id=id).first()
    db.session.delete(cell)
    db.session.commit()
    return redirect(url_for('celular'))

#remover impressora
@app.route("/remover_impressora/<int:id>")
def impremover(id):
    impres = cadastro_impressoras.query.filter_by(id=id).first()
    db.session.delete(impres)
    db.session.commit()
    return redirect(url_for('impressoras'))

#remover monitores
@app.route("/remover_monitores/<int:id>")
def moniremover(id):
    monit = cadastro_monitor.query.filter_by(id=id).first()
    db.session.delete(monit)
    db.session.commit()
    return redirect(url_for('monitores'))

#remover software
@app.route("/remover_software/<int:id>")
def softremover(id):
    softw = cadastro_software.query.filter_by(id=id).first()
    db.session.delete(softw)
    db.session.commit()
    return redirect(url_for('software'))

#remover usuario
@app.route("/remover_usuario/<int:id>")
def usuaremover(id):
    usuary = cadastro_usuario.query.filter_by(id=id).first()
    db.session.delete(usuary)
    db.session.commit()
    return redirect(url_for('usuarios'))

#remover notebook
@app.route("/remover_notebook/<int:id>")
def noteremover(id):
    noteb = cadastro_notebook.query.filter_by(id=id).first()
    db.session.delete(noteb)
    db.session.commit()
    return redirect(url_for('notebook'))

#remover termos
@app.route("/remover_termos/<int:id>")
def removertermos(id):
    termos = file.query.filter_by(id=id).first()
    db.session.delete(termos)
    db.session.commit()
    return redirect(url_for('termo'))

#editar software
@app.route("/editar_software/<int:id>", methods=["GET", "POST"])
def editar_software(id):
    editar = cadastro_software.query.filter_by(id=id).first()
    if request.method=="POST":
        licenca = request.form["licenca"]
        suporte = request.form["suporte"]
        data_renovacao = request.form["data_renovacao"]

        cadastro_software.query.filter_by(id=id).update({
            "licenca": licenca,
            "suporte": suporte,
            "data_renovacao": data_renovacao
        })
        db.session.commit()
        return redirect(url_for('software'))
    return render_template("edita.html", editar=editar)

#editar notebook
@app.route("/editar_notebook/<int:id>", methods=["GET", "POST"])
def editar_notebook(id):
    editar = cadastro_notebook.query.filter_by(id=id).first()
    if request.method=="POST":
        usuarios = request.form["usuario"]
        marca = request.form["marca"]
        mac_adress_fisico= request.form["adressfisico"]
        mac_adress_wifi= request.form["adresswifi"]
        nome_maquina = request.form["maquina"]
        serial = request.form["serial"]
        observacao = request.form["observacao"]
        data_manutencao = request.form["manutencao"]
        data_limite = request.form["limite"]
        
        x = data_limite
        y = data_manutencao
        first = datetime.strptime(x, "%Y-%m-%d").strftime("%d/%m/%Y")
        second = datetime.strptime(y, "%Y-%m-%d").strftime("%d/%m/%Y")
        
        if first < second:
            flash("data incomparaveis")
        else:
            cadastro_notebook.query.filter_by(id=id).update({
                "usuario": usuarios,
                "marca": marca,
                "mac_address_fisico": mac_adress_fisico,
                "mac_address_wifi": mac_adress_wifi,
                "observacao": observacao,
                "nome_maquina": nome_maquina,
                "serial": serial,
                "data_manutencao": second,
                "data_limite": first
            })
            db.session.commit()
            return redirect(url_for('notebook'))
    return render_template("editan.html", editar=editar)

#Editar Celular
@app.route("/edita_celular/<int:id>", methods=["GET", "POST"])
def edita_celular(id):
    edita = cadastro_celulares.query.filter_by(id=id).first()
    if request.method == "POST":
        marca = request.form.get("marca")
        status = request.form.get("status")
        serial = request.form.get("serial")
        usuarios = request.form.get("usuarios")
        imei1 = request.form.get("imei_1")
        imei2 = request.form.get("imei_2")
        
        cadastro_celulares.query.filter_by(id=id).update({
            "marca":marca,
            "status": status,
            "serial": serial,
            "usuarios": usuarios,
            "imei1": imei1,
            "imei2": imei2
        })
        db.session.commit()
        return redirect(url_for('celular'))
    return render_template("editac.html", edita=edita)

#editar usuario
@app.route("/edita_usuario/<int:id>", methods=["GET", "POST"])
def edita_usuario(id):
    edita = cadastro_usuario.query.filter_by(id=id).first()
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        
        cadastro_usuario.query.filter_by(id=id).update({
            "nome": nome,
            "email": email,
            "senha": senha
        })
        db.session.commit()
        return redirect(url_for('usuarios'))
    return render_template("editau.html", edita=edita)
    
#rota home
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/")
def principio():
    return redirect(url_for('home'))

#Logout
@app.route("/logout")
def logout():
    logout_user()
    return render_template("login.html")


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
     