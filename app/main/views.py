from datetime import datetime, timezone
import flask as fk
from . import main
from .. import db
from .forms import CadastrarProfessor
from ..models import Professor
from sqlalchemy import func

# CAMINHOS DO SITE

# Rota Principal
@main.route('/', methods=['GET', 'POST'])
def index():

    return fk.render_template('index.html')

# Rota: Professores
@main.route('/professores', methods=['GET', 'POST'])
def cadastrar_professor():

    cadastro_prof_form = CadastrarProfessor()

    if cadastro_prof_form.validate_on_submit():
        professor = Professor.query.filter_by(nome=cadastro_prof_form.nome.data).first()

        if professor is None:
            professor = Professor(
                nome=cadastro_prof_form.nome.data, 
                disciplina=cadastro_prof_form.disciplina.data
                )

            db.session.add(professor)
            db.session.commit()

            fk.flash("Professor cadastrado com sucesso!")

        else:
            fk.flash("Professor já existe na base de dados!")

        return fk.redirect(fk.url_for('.cadastrar_professor'))

    current_time = datetime.now(timezone.utc)

    return fk.render_template('cadastro_professores.html',
                                current_time=current_time,
                                cadastro_prof_form=cadastro_prof_form
            )

# Rota: Alunos
@main.route('/alunos', methods=['GET', 'POST'])
def cadastrar_aluno():

    return fk.render_template('cadastro_alunos.html')

# Rota: Cursos
@main.route('/cursos', methods=['GET', 'POST'])
def cadastrar_curso():

    return fk.render_template('cadastro_cursos.html')

# Rota: Disciplinas
@main.route('/disciplinas', methods=['GET', 'POST'])
def cadastrar_disciplina():

    return fk.render_template('cadastro_disciplinas.html')

# Rota: Ocorrências
@main.route('/ocorrencias', methods=['GET', 'POST'])
def cadastrar_ocorrencia():

    return fk.render_template('cadastro_ocorrencias.html')
