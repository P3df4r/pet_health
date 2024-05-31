import docker
from pymongo import MongoClient

def register_pet(nome, idade_anos, idade_meses, raca, especie, sexo, alergia, objeto_acompanhado, laudos_anteriores, historico_doencas):
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) #Porta padrão para o biomics
    #client_mongo_database = client_mongo.test
    petdatabase = client_mongo["petdatabase"]
    petdata = petdatabase["petdata"]
    credenciais = {"nome": nome, "idade_anos": idade_anos, "idade_meses": idade_meses, "raca": raca, "especie": especie, "sexo": sexo, "alergia": alergia, "objeto_acompanhado": objeto_acompanhado, "laudos_anteriores": laudos_anteriores, "historico_doencas": historico_doencas}
    petdata.insert_one(credenciais)

def register_tutor(tutor, idade_tutor, endereco_tutor, telefone_tutor):
    tutor = tutor
    idade_tutor = idade_tutor 
    endereco_tutor= endereco_tutor
    telefone_tutor = telefone_tutor

def altered_info_pet(campo, info):
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) #Porta padrão para o biomics
    #client_mongo_database = client_mongo.test
    petdatabase = client_mongo["petdatabase"]
    petdata = petdatabase["petdata"]
    credenciais = {campo: info}
    petdata.insert_one(credenciais)

