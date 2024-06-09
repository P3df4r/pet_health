from pymongo import MongoClient
import docker

def check_consult_date(id_paciente):
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) #Porta padrão para o biomics
    petdatabase = client_mongo["petdatabase"]
    petconsult = petdatabase["petconsult"]
    consulta = {"id": id}
    date = petconsult.find(consulta)
    if date:
        return date
    else:
        return False

def remenber_consult(id_paciente):
    client = docker.DockerClient()
    consult_date = check_consult_date(id_paciente)
    if consult_date:
        container = client.containers.get('pet_heath_mongodb')
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        client_mongo = MongoClient(ip_add) #Porta padrão para o biomics
        petdatabase = client_mongo["petdatabase"]
        petconsult = petdatabase["petconsult"]
        consulta = {"date": consult_date}
        proximity = petconsult.find(consulta)
        if proximity:
            return True
        else:
            return False
 
