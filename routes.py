from flask import Flask, render_template
import pet
import datetime

app = Flask(__name__)

@app.route("/addpet")
def dados():
    nome = ''
    idade_anos = 0
    idade_meses = 0
    raca = ""
    especie = ""
    sexo = False
    alergia = ""
    objeto_acompanhado = ""
    receitas_anteriores = {} 
    procedimentos_realizados = {} 
    consultas_realizadas = [] 
    return pet.register_pet(nome,idade_anos,idade_meses,raca,especie,sexo,alergia,objeto_acompanhado,receitas_anteriores,procedimentos_realizados, consultas_realizadas)

@app.route('/rm_pet')
def rmpet():
    id = 0
    teste = pet.remove_pet(id)
    return teste

@app.route('/alt_pet')
def altpet():
    campo = ''
    info = ''
    id = 0
    return pet.altered_info_pet(campo, info, id)


@app.route('/add_tutor')
def reg_tutor():
    tutor = ''
    idade_tutor = 0
    endereco_tutor = ''
    telefone = ''
    return pet.register_tutor(tutor, idade_tutor, endereco_tutor, telefone)

@app.route('/rm_tutor')
def rmtutor():
    id = ''
    return pet.remove_tutor(id)

@app.route('/alt_tutor')
def alttutor():
    campo = ''
    info = ''
    id = 0
    return pet.altered_info_tutor(campo, info, id)


@app.route('/add_relationship')
def addrel():
    id_pet = ''
    id_tutor = ''
    return pet.register_relationship(id_tutor, id_pet)

#@app.route('/rm_relatioship')
#@app.route('/alt_relationship')

@app.route('/add_consult')
def addconsult():
    id = ''
    data = datetime.datetime(2019, 12, 4)
    return pet.register_consult(id, data)

#@app.route('/rm_consult')
#@app.route('/alt_consult')

@app.route('/add_anamenase')
def addanamenase():
    id_paciente = ''
    last_anamenase = ''
    return pet.register_anamenase(id_paciente,last_anamenase)

@app.route('/see_info_pet', methods=['GET', 'POST'])
def seeinfopet():
    nome = ''
    teste = pet.see_infos_pet(nome)
    return teste

@app.route('/see_info_tutor')
def seeinfotutor():
    nome = ''
    return pet.see_infos_tutor(nome)

@app.route('/create_recipe')
def createrecipe():
    id = ''
    recipe = {}
    return pet.create_recipe(id, recipe)

@app.route('/teste')
def teste():
    return render_template('/home/PH/index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
