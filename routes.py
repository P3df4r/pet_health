from flask import Flask, render_template, request
import pet
import datetime

app = Flask(__name__)

@app.route('/addpet', methods=['GET', 'POST'])
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

@app.route('/rm_pet', methods=['GET', 'POST'])
def rmpet():
    id = ''
    teste = pet.remove_pet(id)
    return teste

@app.route('/alt_pet', methods=['GET', 'POST'])
def altpet():
    campo = ''
    info = ''
    id = 0
    return pet.altered_info_pet(campo, info, id)

@app.route('/add_tutor', methods=['GET', 'POST'])
def reg_tutor():
    tutor = ''
    idade_tutor = 0
    endereco_tutor = ''
    telefone = ''
    return pet.register_tutor(tutor, idade_tutor, endereco_tutor, telefone)

@app.route('/rm_tutor', methods=['GET', 'POST'])
def rmtutor():
    id = ''
    return pet.remove_tutor(id)

@app.route('/alt_tutor', methods=['GET', 'POST'])
def alttutor():
    campo = ''
    info = ''
    id = 0
    return pet.altered_info_tutor(campo, info, id)


@app.route('/add_relationship', methods=['GET', 'POST'])
def addrel():
    id_pet = ''
    id_tutor = ''
    return pet.register_relationship(id_tutor, id_pet)

#@app.route('/rm_relatioship')
#def rm_relationship();
#    id = ''
#    return 

#@app.route('/alt_relationship')

@app.route('/add_consult', methods=['GET', 'POST'])
def addconsult():
    id = ''
    data = datetime.datetime(2019, 12, 4)
    return pet.register_consult(id, data)

#@app.route('/rm_consult')

@app.route('/alt_consult', methods=['GET', 'POST'])
def alt_consult():
    id = ''
    campo = ''
    new_info = ''
    return pet.altered_consult(campo, new_info, id)

@app.route('/add_anamenase', methods=['GET', 'POST'])
def addanamenase():
    id_paciente = ''
    last_anamenase = ''
    return pet.register_anamenase(id_paciente,last_anamenase)

@app.route('/see_info_pet', methods=['GET', 'POST'])
def seeinfopet():
    nome = ''
    teste = pet.see_infos_pet(nome)
    return teste

@app.route('/see_info_tutor', methods=['GET', 'POST'])
def seeinfotutor():
    nome = ''
    return pet.see_infos_tutor(nome)

@app.route('/create_recipe', methods=['GET', 'POST'])
def createrecipe():
    id = ''
    recipe = {}
    return pet.create_recipe(id, recipe)

@app.route('/teste', methods=['GET', 'POST'])
def teste():
    teste = request.get_json()
    print(teste)
    return teste

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
