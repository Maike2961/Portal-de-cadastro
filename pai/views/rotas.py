from app import app, db
from models.model import *
from flask import render_template,redirect,request,flash, url_for
from flask_login import logout_user
from datetime import datetime


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
            salvar =  cadastro_monitor()
            salvar.usuario = usuario
            salvar.etiqueta = etiqueta
            salvar.marca = marca
            salvar.observacao = observacao
            db.session.add(salvar)
            db.session.commit()
    
    monit =  cadastro_monitor.query.all()
        
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
            salvar =  cadastro_impressoras(nome_maquina=nome_maquina, etiqueta=etiqueta, serial=serial, marca=marca, observacao=observacao)
            db.session.add(salvar)
            db.session.commit()
        
    impress =  cadastro_impressoras.query.all()
    return render_template("impressoras.html", impress=impress)
        
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
            salvar =  cadastro_celulares()
            salvar.marca = marca
            salvar.status = status
            salvar.serial = serial
            salvar.usuarios = usuarios
            salvar.imei1 = imei1
            salvar.imei2 = imei2
            db.session.add(salvar)
            db.session.commit() 
    cell =  cadastro_celulares.query.all()
        
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
        x = data_limite
        y = data_manutencao
        first = datetime.strptime(x, "%Y-%m-%d").strftime("%d/%m/%Y")
        second = datetime.strptime(y, "%Y-%m-%d").strftime("%d/%m/%Y")
        
        if first < second:
            flash("data incomparaveis")
            print("datas incomparaveis")
        else:
            salvar =  cadastro_notebook()
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
    
    notes =  cadastro_notebook.query.all()
        
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
            salvar =  cadastro_software()
            salvar.licenca = licenca
            salvar.data_renovacao = data_renovacao2
            salvar.suporte = suporte
            db.session.add(salvar)
            db.session.commit()

    soft =  cadastro_software.query.all()
    
    return render_template("software.html", soft=soft)


#remover celular
@app.route("/remover_celular/<int:id>")
def cellremover(id):
    cell =  cadastro_celulares.query.filter_by(id=id).first()
    db.session.delete(cell)
    db.session.commit()
    return redirect(url_for('celular'))

#remover impressora
@app.route("/remover_impressora/<int:id>")
def impremover(id):
    impres =  cadastro_impressoras.query.filter_by(id=id).first()
    db.session.delete(impres)
    db.session.commit()
    return redirect(url_for('impressoras'))

#remover monitores
@app.route("/remover_monitores/<int:id>")
def moniremover(id):
    monit =  cadastro_monitor.query.filter_by(id=id).first()
    db.session.delete(monit)
    db.session.commit()
    return redirect(url_for('monitores'))

#remover software
@app.route("/remover_software/<int:id>")
def softremover(id):
    softw =  cadastro_software.query.filter_by(id=id).first()
    db.session.delete(softw)
    db.session.commit()
    return redirect(url_for('software'))

#remover usuario
@app.route("/remover_usuario/<int:id>")
def usuaremover(id):
    usuary =  cadastro_usuario.query.filter_by(id=id).first()
    db.session.delete(usuary)
    db.session.commit()
    return redirect(url_for('usuarios'))

#remover notebook
@app.route("/remover_notebook/<int:id>")
def noteremover(id):
    noteb =  cadastro_notebook.query.filter_by(id=id).first()
    db.session.delete(noteb)
    db.session.commit()
    return redirect(url_for('notebook'))


#editar impressora
@app.route("/editar_impressora/<int:id>", methods=["POST", "GET"])
def editar_impressora(id):
    editar =  cadastro_impressoras.query.filter_by(id=id).first()
    if request.method == "POST":
        maquina = request.form["maquina"]
        etiqueta = request.form["etiqueta"]
        serial = request.form["serial"]
        marca = request.form["marca"]
        observacao = request.form["observacao"]
        
        if not maquina or not etiqueta or not serial or not marca or not observacao:
            flash("Por favor, preencha todos os campos")
        else:
            salvar = cadastro_impressoras(nome_maquina=maquina, etiqueta=etiqueta, serial=serial, marca=marca,observacao=observacao)
            db.session.add(salvar)
            db.session.commit()
            flash("Atualizado")
            return redirect(url_for('impressoras'))
    return render_template("editaimpressora.html", editar=editar)

#editar monitor
@app.route("/editar_monitor/<int:id>", methods=["POST", "GET"])
def editar_monitor(id):
    editar =  cadastro_monitor.query.filter_by(id=id).first()
    if request.method == "POST":
        usuario = request.form["usuario"]
        etiqueta = request.form["etiqueta"]
        marca = request.form["marca"]
        observacao = request.form["observacao"]
        
        if not usuario or not etiqueta or not marca or not observacao:
            flash("Por favor, preencha todas as lacunas")
        else:
            salvar =  cadastro_monitor(usuario, etiqueta, marca, observacao)
            db.session.add(salvar)
            db.session.commit()
            return redirect(url_for('monitores'))
    return render_template("editamonit.html", editar=editar)
        
        

#editar software
@app.route("/editar_software/<int:id>", methods=["GET", "POST"])
def editar_software(id):
    editar =  cadastro_software.query.filter_by(id=id).first()
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
    editar =  cadastro_notebook.query.filter_by(id=id).first()
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
    edita =  cadastro_celulares.query.filter_by(id=id).first()
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
    edita =  cadastro_usuario.query.filter_by(id=id).first()
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
