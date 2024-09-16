from bson.errors import InvalidId
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
ip_add = 'localhost:27017'

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
        
        
        
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petdata = petdatabase["petdata"]
        credenciais = {"nome": nome, "idade_anos": idade_anos, "idade_meses": idade_meses, "raca": raca, "especie": especie, "sexo": sexo, "alergia": alergia, "objeto_acompanhado": objeto_acompanhado, "receitas_anteriores": receitas_anteriores, "procedimentos_realizados": procedimentos_realizados, "consultas_realizadas": consultas_realizadas}
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

def register_tutor(tutor, idade_tutor:int, endereco_tutor, telefone_tutor:str):
    try:
        
        
        
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petconsult = petdatabase["pet_tutor"]
        tutor = {"Tutor": tutor, "idade_tutor": idade_tutor, "endereco": endereco_tutor, "telefone": telefone_tutor}
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

def register_relationship(id_tutor:str, id_pet: str):
    try:
        
        
        
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petconsult = petdatabase["pet_relationship"]
        relationship = {"id_tutor": id_tutor, "id_pet": id_pet}
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

def register_consult(id_paciente, date: datetime):
        
        
        
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petconsult = petdatabase["petconsult"]
        consulta = {"ID_paciente": ObjectId(id_paciente), "date": date}
        try:
            petconsult.insert_one(consulta)
        except ValueError:
            return erro_value
        except TypeError:
            return erro_type
        except IndexError:
            return erro_index
        except KeyError:
            return erro_value

def remove_consult(id_paciente):
    try:
        
        
        
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petconsult = petdatabase["petconsult"]
        consulta = {"_id": ObjectId(id_paciente)}
        try:
            petconsult.delete_one(consulta)
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
        return erro_type_consulta
    except IndexError:
        return erro_index
    except KeyError:
        return erro_index

def altered_consult(campo, valor, id_paciente):
    try:
        
        
        
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petconsult = petdatabase["petconsult"]
        consulta = {"_id": ObjectId(id_paciente), campo: valor}
        try:
            petconsult.insert_one(consulta)
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
        return erro_type_consulta
    except IndexError:
        return erro_index
    except KeyError:
        return erro_index

def register_anamenase(id_paciente, last_anamnase: str):
    try:
        
        
        
        client_mongo = MongoClient(ip_add) 
        petdatabase = client_mongo["petdatabase"]
        petanamnase = petdatabase["petanamnase"]
        anamnase = {"_id": id_paciente, "anamnase": last_anamnase}
        try:
            petanamnase.insert_one(anamnase)
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
        return erro_type_anamenase

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
=======
# Registra os dados do pet no banco de dados
def register_pet(nome, idade_anos, idade_meses, raca, especie, sexo: str, alergia: list, objeto_acompanhado: list, receitas_anteriores: dict, procedimentos_realizados: dict, consultas_realizadas: list):
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) 
    petdatabase = client_mongo["petdatabase"]
    petdata = petdatabase["petdata"]
    credenciais = {"nome": nome, "idade_anos": idade_anos, "idade_meses": idade_meses, "raca": raca, "especie": especie, "sexo": sexo, "alergia": alergia, "objeto_acompanhado": objeto_acompanhado, "receitas_anteriores": receitas_anteriores, "procedimentos_realizados": procedimentos_realizados, "consultas_realizadas": consultas_realizadas}
    petdata.insert_one(credenciais)

# Coleta os dados do tutor
def register_tutor(tutor, idade_tutor, endereco_tutor, telefone_tutor):
    tutor = tutor
    idade_tutor = idade_tutor 
    endereco_tutor= endereco_tutor
    telefone_tutor = telefone_tutor

# Registra os dados da consulta no banco de dados
def register_consult(id_paciente, diagnostico: list, date: int):
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) 
    petdatabase = client_mongo["petdatabase"]
    petconsult = petdatabase["petconsult"]
    consulta = {"_id": id_paciente, "diagnostico": diagnostico, "date": date}
    petconsult.insert_one(consulta)

# Registra os dados da anamenase no banco de dados
def register_anamenase(id_paciente, last_anamnase):
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) 
    petdatabase = client_mongo["petdatabase"]
    petanamnase = petdatabase["petanamnase"]
    anamnase = {"_id": id_paciente, "anamnase": last_anamnase}
    petanamnase.insert_one(anamnase)

# Atualiza informações do pet no banco de dados
def altered_info_pet(campo, info):
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) 
    petdatabase = client_mongo["petdatabase"]
    petdata = petdatabase["petdata"]
    credenciais = {campo: info}
    petdata.insert_one(credenciais)

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
    client = docker.DockerClient()
    container = client.containers.get('pet_heath_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client_mongo = MongoClient(ip_add) 
    petdatabase = client_mongo["petdatabase"]
    petdata = petdatabase["petdata"]
    receitas = {"_id": id,  "receitas_anteriores":indicacoes}
    petdata.insert_one(receitas)

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