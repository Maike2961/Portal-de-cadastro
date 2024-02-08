from app import *

class cadastro_monitor(db.Model):
    __tablename__="monitor"
    id = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String(100), nullable=False)
    etiqueta = db.Column(db.Integer)
    marca = db.Column(db.String(100))
    observacao = db.Column(db.String(100))
     
    def __init__(self, usuario, etiqueta, marca, observacao):
        self.usuario = usuario
        self.etiqueta = etiqueta
        self.marca = marca
        self.observacao = observacao

class cadastro_impressoras(db.Model):
    __tablename__ ="impressoras"
    id =db.Column(db.Integer,primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    etiqueta = db.Column(db.String(80), nullable=False)
    nome_maquina = db.Column(db.String(100), nullable=False)
    serial = db.Column(db.String(80), nullable=False)
    observacao = db.Column(db.String(100))
    
    def __init__(self, marca, etiqueta, serial, nome_maquina, observacao):
        self.marca = marca
        self.etiqueta = etiqueta
        self.nome_maquina = nome_maquina
        self.serial = serial
        self.observacao = observacao

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