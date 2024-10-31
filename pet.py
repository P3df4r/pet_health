from bson.errors import InvalidId
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
import docker

options_mongo = '$options'
regex_mongo = '$regex'
erro_value = 'Um dos valores inseridos está incorreto'
erro_type = 'Não foi possivel adicionar o pet'
erro_index = 'Um dos campos não foi preenchido'
erro_type_tutor = "Não foi possivel adicionar o tutor"
erro_type_anamenase = "Não foi possivel adicionar a anamenase"
erro_type_relationship = "Não foi possivel adicionar a relação"
erro_type_consulta = "Não foi possivel adicionar a consulta"
ip_add = 'localhost:27017'

def register_pet(nome: str, 
                 idade:int,
                 peso: float,
                 especie: str, 
                 sexo: bool,
                 id_tutor: int):
    try:
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petdata = petdatabase["petdata"]
        credenciais = {"nome": nome, "idade": idade, "peso": peso, "especie": especie, "sexo": sexo, "id_tor": id_tutor}
        try:
            petdata.insert_one(credenciais)
            return 'Inserido com sucesso'
        except ValueError:
            return erro_value
        except TypeError:
            return erro_type
        except IndexError:
            return erro_index
        except KeyError:
            return erro_value
    except TypeError:
        return erro_type
    except IndexError:
        return erro_index
    except KeyError:
        return erro_index

def remove_pet(id):
    try: 
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petdata = petdatabase["petdata"]
        try:
            confirm_remove = petdata.delete_one({"_id": ObjectId(id)})
            if confirm_remove:
                return 'Removido com sucesso'
        except ValueError:
            return erro_value
        except TypeError:
            return erro_type
        except IndexError:
            return erro_index
        except KeyError:
            return erro_value 
    except InvalidId:
        return erro_value
    except TypeError:
        return erro_type
    except IndexError:
        return erro_index
    except KeyError:
        return erro_index

def altered_info_pet(campo:str, info:str, id):
    try:
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petdata = petdatabase["petdata"]
        credenciais = {'_id': ObjectId(id), campo: {regex_mongo: info, options_mongo: "i"}}
        try:
            petdata.insert_one(credenciais)
            return 'Modificado com sucesso'
        except ValueError:
            return erro_value
        except TypeError:
            return erro_type
        except IndexError:
            return erro_index
        except KeyError:
            return erro_value
    except InvalidId:
        return erro_value
    except TypeError:
        return "Não foi possivel alterar a informação do pet"
    except IndexError:
        return erro_index
    except KeyError:
        return erro_index

def register_tutor(tutor, endereco_tutor, telefone_tutor:str, email, cpf):
    try:
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petconsult = petdatabase["pet_tutor"]
        tutor = {"Tutor": tutor, "email": email, "endereco": endereco_tutor, "telefone": telefone_tutor, "cpf": cpf}
        try:
            petconsult.insert_one(tutor)
            return 'Inserido com sucesso'
        except ValueError:
            return erro_value
        except TypeError:
            return erro_type
        except IndexError:
            return erro_index
        except KeyError:
            return erro_value
    except TypeError:
        return erro_type_tutor

def remove_tutor(id):
    try:
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petconsult = petdatabase["pet_tutor"]
        tutor = {"_id": id}
        try:
            petconsult.delete_one(tutor)
            return 'Removido com sucesso'
        except ValueError:
            return erro_value
        except TypeError:
            return erro_type
        except IndexError:
            return erro_index
        except KeyError:
            return erro_value
    except InvalidId:
        return erro_value
    except TypeError:
        return erro_type_tutor

def altered_info_tutor(campo:str, info:str, id):
    try:
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petdata = petdatabase["pet_tutor"]
        credenciais = {'_id': ObjectId(id), campo: {regex_mongo: info, options_mongo: "i"}}
        try:
            petdata.insert_one(credenciais)
            return 'Alterado com sucesso'
        except ValueError:
            return erro_value
        except TypeError:
            return erro_type
        except IndexError:
            return erro_index
        except KeyError:
            return erro_value
    except InvalidId:
        return erro_value
    except TypeError:
        return "Não foi possivel alterar a informação do tutor"
    except IndexError:
        return erro_index
    except KeyError:
        return erro_index

def add_ficha(id_pet: str, obs, id_hist_clin):
    try:
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petconsult = petdatabase["pet_relationship"]
        relationship = {"id_pet": id_pet, "obs": obs, "id_hist_clin": id_hist_clin}
        try:
            petconsult.insert_one(relationship)
            return 'Inserido com sucesso'
        except ValueError:
            return erro_value
        except TypeError:
            return erro_type
        except IndexError:
            return erro_index
        except KeyError:
            return erro_value
    except TypeError:
        return erro_type_relationship

def add_hist_clin(alergia: str, cirurgia: str, exame: str, medicamento: str, suplementacao: str):
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petconsult = petdatabase["petconsult"]
        hist_clin = {"alergia":alergia,"cirurgia":cirurgia,"exame":exame,"medicamento":medicamento,"suplementacao":suplementacao}
        try:
            petconsult.insert_one(hist_clin)
        except ValueError:
            return erro_value
        except TypeError:
            return erro_type
        except IndexError:
            return erro_index
        except KeyError:
            return erro_value

def see_infos_pet(search:str):
        client_mongo = MongoClient('localhost:27017') 
        petdatabase = client_mongo["petdatabase"]
        petdata = petdatabase["petdata"]
        credenciais = {"nome": {regex_mongo: search, options_mongo: "i"}}
        if petdata.find_one(credenciais) is not None:
            for x in petdata.find(credenciais):
                for coluna, valor in x.items():
                    return coluna + ":", valor
        else:
            return 'não existe' 

def see_infos_tutor(search:str):
    try:
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petdata = petdatabase["pet_tutor"]
        credenciais = {"Tutor": {regex_mongo: search, options_mongo: "i"}}
        try:
            for x in petdata.find(credenciais):
                return str(x)
        except ValueError:
            return erro_value
        except TypeError:
            return erro_type
        except IndexError:
            return erro_index
        except KeyError:
            return erro_value
    except InvalidId:
        return erro_value
    except TypeError:
        return "Não foi possivel verificar as informações"

# Lê as informações do pet no banco de dados
def see_infos(id):
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) 
    petdatabase = client_mongo["petdatabase"]
    petdata = petdatabase["petdata"]
    credenciais = {"_id": id}
    petdata.find(credenciais)


# Registra as receitas no banco de dados
def create_recipe(id, indicacoes: dict):
    try:    
        client = docker.DockerClient()
        container = client.containers.get('pet_heath_mongodb')
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petdata = petdatabase["petdata"]
        receitas = {"_id": id,  "receitas_anteriores":indicacoes}
        try:
            petdata.insert_one(receitas)
            return 'Criado com sucesso'
        except ValueError:
            return erro_value
        except TypeError:
            return erro_type
        except IndexError:
            return erro_index
        except KeyError:
            return erro_value
    except TypeError:
        return "Não foi possivel criar a receita"
    except IndexError:
        return erro_index
    except KeyError:
        return erro_index

# Lê os dados da anamenase
def see_anamenase(id):
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) 
    petdatabase = client_mongo["petdatabase"]
    petanamnase = petdatabase["petanamnase"]
    anamenase = {"_id": id}
    petanamnase.find(anamenase)

# Atualiza os dados da anamenase no banco de dados
def altered_info_anamenase(campo, info):
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) 
    petdatabase = client_mongo["petdatabase"]
    petanamnase = petdatabase["petanamnase"]
    anamenase = {campo: info}
    petanamnase.insert_one(anamenase)

# deleta os dados da anamenase no banco de dados
def delete_anamenase(id):
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) 
    petdatabase = client_mongo["petdatabase"]
    petanamnase = petdatabase["petanamnase"]
    anamenase = {"_id": id}
    petanamnase.delete_one(anamenase)
