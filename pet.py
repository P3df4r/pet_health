from bson.errors import InvalidId
import docker
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId

options_mongo = '$options'
regex_mongo = '$regex'
erro_value = 'Um dos valores inseridos está incorreto'
erro_type = 'Não foi possivel adicionar o pet'
erro_index = 'Um dos campos não foi preenchido'
erro_type_tutor = "Não foi possivel adicionar o tutor"
erro_type_anamenase = "Não foi possivel adicionar a anamenase"
erro_type_relationship = "Não foi possivel adicionar a relação"
erro_type_consulta = "Não foi possivel adicionar a consulta"

def register_pet(nome: str, 
                 idade_anos:int, 
                 idade_meses: int, 
                 raca: str, 
                 especie: str, 
                 sexo: bool, 
                 alergia: str, 
                 objeto_acompanhado: str, 
                 receitas_anteriores: dict, 
                 procedimentos_realizados: dict, consultas_realizadas: list):
    try:
        client = docker.DockerClient()
        container = client.containers.get('pet_health_mongodb')
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petdata = petdatabase["petdata"]
        credenciais = {"nome": nome, "idade_anos": idade_anos, "idade_meses": idade_meses, "raca": raca, "especie": especie, "sexo": sexo, "alergia": alergia, "objeto_acompanhado": objeto_acompanhado, "receitas_anteriores": receitas_anteriores, "procedimentos_realizados": procedimentos_realizados, "consultas_realizadas": consultas_realizadas}
        try:
            petdata.insert_one(credenciais)
        except ValueError:
            print(erro_value)
        except TypeError:
            print(erro_type)
        except IndexError:
            print(erro_index)
        except KeyError:
            print(erro_value)
    except TypeError:
        print(erro_type)
    except IndexError:
        print(erro_index)
    except KeyError:
        print(erro_index)

def remove_pet(id):
    try: 
        client = docker.DockerClient()
        container = client.containers.get('pet_health_mongodb')
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petdata = petdatabase["petdata"]
        try:
            confirm_remove = petdata.delete_one({"_id": ObjectId(id)})
            if confirm_remove:
                print('Removido com sucesso')
        except ValueError:
            print(erro_value)
        except TypeError:
            print(erro_type)
        except IndexError:
            print(erro_index)
        except KeyError:
            print(erro_value) 
    except InvalidId:
        print(erro_value)
    except TypeError:
        print(erro_type)
    except IndexError:
        print(erro_index)
    except KeyError:
        print(erro_index)

def altered_info_pet(campo:str, info:str, id):
    try:
        client = docker.DockerClient()
        container = client.containers.get('pet_health_mongodb')
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petdata = petdatabase["petdata"]
        credenciais = {'_id': ObjectId(id), campo: {regex_mongo: info, options_mongo: "i"}}
        try:
            petdata.insert_one(credenciais)
        except ValueError:
            print(erro_value)
        except TypeError:
            print(erro_type)
        except IndexError:
            print(erro_index)
        except KeyError:
            print(erro_value)
    except InvalidId:
        print(erro_value)
    except TypeError:
        print("Não foi possivel alterar a informação do pet")
    except IndexError:
        print(erro_index)
    except KeyError:
        print(erro_index)

def register_tutor(tutor, idade_tutor:int, endereco_tutor, telefone_tutor:int):
    try:
        client = docker.DockerClient()
        container = client.containers.get('pet_health_mongodb')
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petconsult = petdatabase["pet_tutor"]
        tutor = {"Tutor": tutor, "idade_tutor": idade_tutor, "endereco": endereco_tutor, "telefone": telefone_tutor}
        try:
            petconsult.insert_one(tutor)
        except ValueError:
            print(erro_value)
        except TypeError:
            print(erro_type)
        except IndexError:
            print(erro_index)
        except KeyError:
            print(erro_value)
    except TypeError:
        print(erro_type_tutor)

def remove_tutor(id):
    try:
        client = docker.DockerClient()
        container = client.containers.get('pet_health_mongodb')
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petconsult = petdatabase["pet_tutor"]
        tutor = {"_id": id}
        try:
            petconsult.delete_one(tutor)
        except ValueError:
            print(erro_value)
        except TypeError:
            print(erro_type)
        except IndexError:
            print(erro_index)
        except KeyError:
            print(erro_value)
    except InvalidId:
        print(erro_value)
    except TypeError:
        print(erro_type_tutor)

def altered_info_tutor(campo:str, info:str, id):
    try:
        client = docker.DockerClient()
        container = client.containers.get('pet_health_mongodb')
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petdata = petdatabase["pet_tutor"]
        credenciais = {'_id': ObjectId(id), campo: {regex_mongo: info, options_mongo: "i"}}
        try:
            petdata.insert_one(credenciais)
        except ValueError:
            print(erro_value)
        except TypeError:
            print(erro_type)
        except IndexError:
            print(erro_index)
        except KeyError:
            print(erro_value)
    except InvalidId:
        print(erro_value)
    except TypeError:
        print("Não foi possivel alterar a informação do tutor")
    except IndexError:
        print(erro_index)
    except KeyError:
        print(erro_index)

def register_relationship(id_tutor:str, id_pet: str):
    try:
        client = docker.DockerClient()
        container = client.containers.get('pet_health_mongodb')
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petconsult = petdatabase["pet_relationship"]
        relationship = {"id_tutor": id_tutor, "id_pet": id_pet}
        try:
            petconsult.insert_one(relationship)
        except ValueError:
            print(erro_value)
        except TypeError:
            print(erro_type)
        except IndexError:
            print(erro_index)
        except KeyError:
            print(erro_value)
    except TypeError:
        print(erro_type_relationship)

def register_consult(id_paciente, date: datetime):
        client = docker.DockerClient()
        container = client.containers.get('pet_health_mongodb')
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petconsult = petdatabase["petconsult"]
        consulta = {"ID_paciente": ObjectId(id_paciente), "date": date}
        try:
            petconsult.insert_one(consulta)
        except ValueError:
            print(erro_value)
        except TypeError:
            print(erro_type)
        except IndexError:
            print(erro_index)
        except KeyError:
            print(erro_value)

def remove_consult(id_paciente):
    try:
        client = docker.DockerClient()
        container = client.containers.get('pet_health_mongodb')
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petconsult = petdatabase["petconsult"]
        consulta = {"_id": ObjectId(id_paciente)}
        try:
            petconsult.delete_one(consulta)
        except ValueError:
            print(erro_value)
        except TypeError:
            print(erro_type)
        except IndexError:
            print(erro_index)
        except KeyError:
            print(erro_value)
    except InvalidId:
        print(erro_value)
    except TypeError:
        print(erro_type_consulta)
    except IndexError:
        print(erro_index)
    except KeyError:
        print(erro_index)

def altered_consult(campo, valor, id_paciente):
    try:
        client = docker.DockerClient()
        container = client.containers.get('pet_health_mongodb')
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petconsult = petdatabase["petconsult"]
        consulta = {"_id": ObjectId(id_paciente), campo: valor}
        try:
            petconsult.insert_one(consulta)
        except ValueError:
            print(erro_value)
        except TypeError:
            print(erro_type)
        except IndexError:
            print(erro_index)
        except KeyError:
            print(erro_value)
    except InvalidId:
        print(erro_value)
    except TypeError:
        print(erro_type_consulta)
    except IndexError:
        print(erro_index)
    except KeyError:
        print(erro_index)

def register_anamenase(id_paciente, last_anamnase: str):
    try:
        client = docker.DockerClient()
        container = client.containers.get('pet_health_mongodb')
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petanamnase = petdatabase["petanamnase"]
        anamnase = {"_id": id_paciente, "anamnase": last_anamnase}
        try:
            petanamnase.insert_one(anamnase)
        except ValueError:
            print(erro_value)
        except TypeError:
            print(erro_type)
        except IndexError:
            print(erro_index)
        except KeyError:
            print(erro_value)
    except TypeError:
        print(erro_type_anamenase)

def see_infos_pet(search:str):
        client = docker.DockerClient()
        container = client.containers.get('pet_health_mongodb')
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petdata = petdatabase["petdata"]
        credenciais = {"nome": {regex_mongo: search, options_mongo: "i"}}
        if petdata.find_one(credenciais) is not None:
            for x in petdata.find(credenciais):
                for coluna, valor in x.items():
                    print(coluna + ":", valor)
        else:
            assert petdatabase.find_one(credenciais) is None, 'Erro'
   
def see_infos_tutor(search:str):
    try:
        client = docker.DockerClient()
        container = client.containers.get('pet_health_mongodb')
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petdata = petdatabase["pet_tutor"]
        credenciais = {"Tutor": {regex_mongo: search, options_mongo: "i"}}
        try:
            for x in petdata.find(credenciais):
                for coluna, valor in x.items():
                    print(coluna + ":", valor)
        except ValueError:
            print(erro_value)
        except TypeError:
            print(erro_type)
        except IndexError:
            print(erro_index)
        except KeyError:
            print(erro_value)
    except InvalidId:
        print(erro_value)
    except TypeError:
        print("Não foi possivel verificar as informações")

def create_recipe(id, indicacoes: dict):
    try:
        client = docker.DockerClient()
        container = client.containers.get('pet_health_mongodb')
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petdata = petdatabase["petdata"]
        receitas = {"_id": id,  "receitas_anteriores":indicacoes}
        try:
            petdata.insert_one(receitas)
        except ValueError:
            print(erro_value)
        except TypeError:
            print(erro_type)
        except IndexError:
            print(erro_index)
        except KeyError:
            print(erro_value)
    except TypeError:
        print("Não foi possivel criar a receita")
    except IndexError:
        print(erro_index)
    except KeyError:
        print(erro_index)

