from . import db


class FeirasLivres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_ = db.Column(db.String(100))
    lat = db.Column(db.String(100))
    setcens = db.Column(db.String(100))
    areap = db.Column(db.String(100))
    coddist = db.Column(db.String(100))
    distrito = db.Column(db.String(100))
    codsubprefe = db.Column(db.String(100))
    subprefe = db.Column(db.String(100))
    regiao5 = db.Column(db.String(100))
    regiao8 = db.Column(db.String(100))
    nome_feira = db.Column(db.String(100))
    registro = db.Column(db.String(100))
    logradouro = db.Column(db.String(100))
    numero = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    referencia = db.Column(db.String(100))
