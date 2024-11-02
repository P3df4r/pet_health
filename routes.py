from flask import Flask, request
import pet

app = Flask(__name__)

@app.route('/addpet', methods=['GET', 'POST'])
def addpet():
    data = request.get_json()
    nome = data['nome']
    idade = data['idade']
    peso = data['idade']
    especie = data['especie']
    id_tutor = data['ID_tutor']
    sexo = data['sexo']
    return pet.register_pet(nome, idade, peso, especie, id_tutor, sexo) 

@app.route('/rm_pet', methods=['GET', 'POST'])
def rmpet():
    data = request.get_json()
    id = data['id'] 
    teste = pet.remove_pet(id)
    return teste

@app.route('/add_tutor', methods=['GET', 'POST'])
def reg_tutor():
    data = request.get_json()
    tutor = data['nome']
    endereco_tutor = data['endereco_tutor']
    telefone = data['telefone']
    email = data['email']
    cpf = data['cpf']
    return pet.register_tutor(tutor, email, endereco_tutor, cpf, telefone)

@app.route('/rm_tutor', methods=['GET', 'POST'])
def rmtutor():
    data = request.get_json()
    id = data['id']
    return pet.remove_tutor(id)

@app.route('/add_anamenase', methods=['GET', 'POST'])
def addficha():
    data = request.get_json()
    id_paciente = data['id_tutelado']
    obs = data['observacoes']
    id_hist_clin = data['id_hist_clin']
    return pet.add_ficha(id_paciente, obs, id_hist_clin)

@app.route('/hist_clin', methods=['GET', 'POST'])
def hist_clin():
    data = request.get_json()
    alergia = data['alergia']
    cirurgia = data['cirurgia']
    exame = data['exame']
    medicamento = data['medicamento']
    suplementacao = data['suplementacao']
    return pet.add_hist_clin(alergia, cirurgia, exame, medicamento, suplementacao)

@app.route('/see_info_tutor', methods=['GET', 'POST'])
def seeinfotutor():
    nome = ''
    return pet.see_infos_tutor(nome)

@app.route('/see_info_pet', methods=['GET', 'POST'])
def seeinfopet():
    nome = ''
    return pet.see_infos_pet(nome)

@app.route('/teste', methods=['GET'])
def teste():
    #teste = request.get_json()
    return 'teste'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int("4002")) 
