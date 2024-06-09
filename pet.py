import docker
from pymongo import MongoClient

def register_pet(nome, idade_anos, idade_meses, raca, especie, sexo: str, alergia: list, objeto_acompanhado: list, receitas_anteriores: dict, procedimentos_realizados: dict, consultas_realizadas: list):
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) 
    petdatabase = client_mongo["petdatabase"]
    petdata = petdatabase["petdata"]
    credenciais = {"nome": nome, "idade_anos": idade_anos, "idade_meses": idade_meses, "raca": raca, "especie": especie, "sexo": sexo, "alergia": alergia, "objeto_acompanhado": objeto_acompanhado, "receitas_anteriores": receitas_anteriores, "procedimentos_realizados": procedimentos_realizados, "consultas_realizadas": consultas_realizadas}
    petdata.insert_one(credenciais)

def register_tutor(tutor, idade_tutor, endereco_tutor, telefone_tutor):
    tutor = tutor
    idade_tutor = idade_tutor 
    endereco_tutor= endereco_tutor
    telefone_tutor = telefone_tutor

def register_consult(id_paciente, diagnostico: list, date: int):
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) 
    petdatabase = client_mongo["petdatabase"]
    petconsult = petdatabase["petconsult"]
    consulta = {"_id": id_paciente, "diagnostico": diagnostico, "date": date}
    petconsult.insert_one(consulta)

def register_anamenase(id_paciente, last_anamnase):
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) 
    petdatabase = client_mongo["petdatabase"]
    petanamnase = petdatabase["petanamnase"]
    anamnase = {"_id": id_paciente, "anamnase": last_anamnase}
    petanamnase.insert_one(anamnase)

def altered_info_pet(campo, info):
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) 
    petdatabase = client_mongo["petdatabase"]
    petdata = petdatabase["petdata"]
    credenciais = {campo: info}
    petdata.insert_one(credenciais)

def see_infos(id):
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) 
    petdatabase = client_mongo["petdatabase"]
    petdata = petdatabase["petdata"]
    credenciais = {"_id": id}
    petdata.find(credenciais)

def create_recipe(id, indicacoes: dict):
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) 
    petdatabase = client_mongo["petdatabase"]
    petdata = petdatabase["petdata"]
    receitas = {"_id": id,  "receitas_anteriores":indicacoes}
    petdata.insert_one(receitas)

