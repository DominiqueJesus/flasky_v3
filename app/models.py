from . import db
from datetime import datetime, timezone

class Professor(db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True, index=True)
    disciplina = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<Professor %r>' % self.nome
