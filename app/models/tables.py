from app import db

class Noticia(db.Model):
    __tablename__ = "noticias"

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String, unique=True)
    titulo = db.Column(db.String)
    data = db.Column(db.String)

    def __init__(self, link, titulo, data):
        self.link = link
        self.titulo = titulo
        self.data = data

    def __repr__(self):
        return "<Noticia Tecmundo: %r>" % self.link

class Mega(db.Model):
    __tablename__ = "mega"

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String, unique=True)
    titulo = db.Column(db.String)
    categoria = db.Column(db.String)

    def __init__(self, link, titulo, categoria):
        self.link = link
        self.titulo = titulo
        self.categoria = categoria

    def __repr__(self):
        return "<Noticia Megacurioso: %r>" % self.link


