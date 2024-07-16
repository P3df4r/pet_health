from bson.errors import InvalidId
from pymongo import MongoClient
import docker
from bson.objectid import ObjectId

erro_value = 'Valor indevido inserido'
erro_type = 'Tipo indevido de dado inserido'
erro_index = 'Erro ao adicionar definição do valor'
erro_key = 'Erro ao adicionar valor'

def check_consult_date(id_paciente):
    try:
        client = docker.DockerClient()
        container = client.containers.get('pet_health_mongodb')
        ip_add = container.attrs['NetworkSettings']['IPAddress']
        client_mongo = MongoClient(ip_add)
        petdatabase = client_mongo["petdatabase"]
        petconsult = petdatabase["petconsult"]
        consulta = {"_id": ObjectId(id_paciente)}
        try:
            print(petconsult.find_one())
            for x in petconsult.find(consulta):
                for coluna, valor in x.items():
                    print(coluna + ":", valor)
        except ValueError:
            print(erro_value)
        except TypeError:
            print(erro_type)
        except IndexError:
            print(erro_index)
        except KeyError:
            print(erro_key)
    except InvalidId:
        print(erro_value)
    except ValueError:
        print(erro_value)
    except TypeError:
        print(erro_type)
    except IndexError:
        print(erro_index)
    except KeyError:
        print(erro_key)

def remenber_consult(id_paciente):
    try:
        client = docker.DockerClient()
        consult_date = check_consult_date(id_paciente)
        if consult_date:
            container = client.containers.get('pet_health_mongodb')
            ip_add = container.attrs['NetworkSettings']['IPAddress']
            client_mongo = MongoClient(ip_add) #Porta padrão para o biomics
            petdatabase = client_mongo["petdatabase"]
            petconsult = petdatabase["petconsult"]
            consulta = {"date": consult_date}
            try:
                petconsult.find(consulta)
            except ValueError:
                print(erro_value)
            except TypeError:
                print(erro_type)
            except IndexError:
                print(erro_index)
            except KeyError:
                print(erro_key)
    except InvalidId:
        print(erro_value)
    except ValueError:
        print(erro_value)
    except TypeError:
        print(erro_type)
    except IndexError:
        print(erro_index)
    except KeyError:
        print(erro_key)

