from bson.errors import InvalidId
import pet
import vet
from datetime import datetime
from art import tprint
from time import sleep
import os
import docker
   
options_mongo = '$options'
regex_mongo = '$regex'
titulo = 'PET HEALTH'
erro_valor = 'Valor inserido incorretamente'
erro_key = 'Erro ao adicionar valor'
erro_index = 'Erro ao adicionar definição do valor'
erro_type = 'Usuario nao encontrado '
nome_pet = 'Digite o nome do PET: '
nome_tutor = 'Digite o nome do Tutor: '
id_pet = 'Digite o ID do PET: ' 
id_tutor = 'Digite o ID do Tutor: ' 
insert_option_view = 'Digite a opção correspondente: '
return_men = 'Deseja retornar? Aperte 0 para retornar: '
camp_name = 'Qual o nome do campo a ser alterado: '
new_value = 'Digite o novo valor: '

menu_inicial = '''
1 - Menu PET
2 - Menu Veterinário
0 - Sair
'''

menu_relacao = '''
O tutor ja possui pet cadastrado?

1 - Sim
2 - Não
'''

menu_pet = '''
1 - PET
2 - Tutor
3 - Consulta
4 - Anamenase
5 - Ver informações
6 - Criar receita
0 - Voltar
'''

menu_crud_pet = '''
1 - Cadastrar PET
2 - Ver PET
3 - Remover PET
4 - Alterar PET
0 - Voltar
'''

crud_tutor_variaveis = '''
1 - Cadastrar tutor
2 - Ver tutor
3 - Remover tutor
4 - Alterar tutor
0 - Voltar
'''

menu_vet = '''
1 - Checar consulta
2 - Relembrar consulta
0 - Voltar
'''

add_mais_medicamento = '''
Adicionar mais medicamentos?
1 - Sim
2 - Não
'''

menu_crud_conuslta = '''
1 - Cadastrar consulta
2 - Remover consulta
3 - Alterar consulta
0 - Voltar
'''

def check_database():
    client = docker.DockerClient()
    container = client.containers.get('pet_health_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    if not ip_add:
            os.system('clear')
            tprint(titulo)
            print('Banco de dados desligado')
            exit()


def crud_consulta():
    try:
        os.system('clear')
        tprint(titulo)
        print(menu_crud_conuslta)
        escolha_consulta = int(input(insert_option_view))
        if escolha_consulta == 1:
            busca_nome = str(input(nome_pet))
            pet.see_infos_pet(busca_nome)
            escolha_id = str(input(id_pet))
            dia = int(input('Digite o dia da consulta: '))
            mes = int(input('Digite o mes da consulta: '))
            ano = int(input('Digite o ano da consulta: '))
            data = datetime(ano, mes, dia)
            pet.register_consult(escolha_id, data) 
            escolha_consulta = int(input(return_men))
        if escolha_consulta == 2:
            busca_nome = str(input(nome_pet))
            pet.see_infos_pet(busca_nome)
            escolha_id = str(input(return_men))
            vet.check_consult_date(escolha_id)
            pet.remove_consult(input('Digite o ID da consulta a ser retirada: '))
            escolha_consulta = int(input(return_men))
        if escolha_consulta == 3:
            nome_pet_local = str(input(nome_pet))
            pet.see_infos_pet(nome_pet_local)
            id_local = str(input(id_pet))
            print(vet.check_consult_date(id_local))
            campo = str(input(camp_name))
            valor = str(input(new_value))
            pet.altered_consult(campo, valor, id_local)
            escolha_consulta = int(input(return_men))
    except ValueError:
        os.system('clear')
        tprint(titulo)
        print(erro_valor)
        sleep(5)
        os.system('clear')
    except TypeError:
        os.system('clear')
        tprint(titulo)
        print(erro_type)
        sleep(5)        
        os.system('clear')
    except IndexError:
        os.system('clear')
        tprint(titulo)
        print(erro_index)
        sleep(5)
        os.system('clear')
    except KeyError:
        os.system('clear')
        tprint(titulo)
        print(erro_key)
        sleep(5)
        os.system('clear')

def crud_pet():
    try:
        os.system('clear')
        tprint(titulo)
        print(menu_crud_pet)
        escolha_pet = int(input(insert_option_view))
        if escolha_pet == 1:
            nome_pet_local = str(input(nome_pet))
            idade_ano_pet = int(input('Digite a idade em anos do pet: '))
            idade_mes_pet = int(input("Digite a idade em meses do pet: "))
            raca_pet = str(input('Digite a raça do pet: '))
            especie_pet = str(input('Digite a especie do pet: '))
            sexo_pet = bool(input('Digite o sexo do pet: '))
            alergia = str(input('Digite as alergias do pet: '))
            objeto_pet = str(input('Digite algum objeto que o pet possua: '))
            receitas_pet = {}
            procedimentos_pet = {}
            consultas_realizadas = []
            pet.register_pet(nome_pet_local,
                             idade_ano_pet, 
                             idade_mes_pet,
                             raca_pet,
                             especie_pet,
                             sexo_pet,
                             alergia,
                             objeto_pet,
                             receitas_pet,
                             procedimentos_pet,
                             consultas_realizadas)
            os.system('clear')
        if escolha_pet == 2:
            nome_pet_local = str(input(nome_pet))
            pet.see_infos_pet(nome_pet_local)
            escolha_pet = str(input(return_men))
        if escolha_pet == 3:
            nome_pet_local = str(input(nome_pet))
            pet.see_infos_pet(nome_pet_local)
            id_local = str(input(id_pet))
            pet.remove_pet(id_local)
            escolha_pet = int(input(return_men))
        if escolha_pet == 4:
            nome_pet_local = str(input(nome_pet))
            pet.see_infos_pet(nome_pet_local)
            id_local = str(input(id_pet))
            campo = input(camp_name)
            valor = input(new_value)
            pet.altered_info_pet(campo, valor, id_local)
            escolha_pet = int(input(return_men))
    except (ValueError, InvalidId):
        os.system('clear')
        tprint(titulo)
        print(erro_valor)
        sleep(5)
        os.system('clear')
    except TypeError:
        os.system('clear')
        tprint(titulo)
        print(erro_type)
        sleep(5)        
        os.system('clear')
    except IndexError:
        os.system('clear')
        tprint(titulo)
        print(erro_index)
        sleep(5)
        os.system('clear')
    except KeyError:
        os.system('clear')
        tprint(titulo)
        print(erro_key)
        sleep(5)
        os.system('clear')

def crud_tutor():
    try:
        os.system('clear')
        tprint(titulo)
        print(crud_tutor_variaveis)
        escolha_tutor = int(input(insert_option_view))
        if escolha_tutor == 1:
            nome_tutor_local1 = str(input(nome_tutor))
            idade_tutor = int(input('Digite a idade do tutor: '))
            endereco_tutor = str(input('Digite o endereço do tutor: '))
            telefone_tutor = int(input('Digite o telefone do tutor: '))
            pet.register_tutor(nome_tutor_local1, idade_tutor, endereco_tutor, telefone_tutor)
            relacionar = int(input(menu_relacao))
            if relacionar == 1:
                nome_pet_local = input(nome_pet)
                pet.see_infos_pet(nome_pet_local)
                id_pet_temp = input(id_pet)
                pet.see_infos_tutor(nome_tutor_local1)
                id_tutor_temp = input(id_tutor)
                pet.register_relationship(id_tutor_temp, id_pet_temp)
            escolha_tutor = int(input(return_men))
        if escolha_tutor == 2:
            nome_tutor_local = str(input(nome_tutor))
            pet.see_infos_tutor(nome_tutor_local)
            escolha_tutor = str(input(return_men))
        if escolha_tutor == 3:
            nome_tutor_local = str(input('Digite o nome do tutor: '))
            nome_pet_local = str(input(nome_tutor))
            pet.see_infos_tutor(nome_pet_local)
            id_local = str(input(id_tutor))
            pet.remove_tutor(id_local) 
            escolha_tutor = int(input(return_men))
        if escolha_tutor == 4:
            nome_tutor_local = str(input(nome_tutor))
            pet.see_infos_tutor(nome_tutor_local)
            id_local = str(input(id_tutor))
            campo = input(camp_name)
            valor = input(new_value)
            pet.altered_info_tutor(campo, valor, id)
            escolha_tutor = int(input(return_men))
    except (ValueError, InvalidId):
        os.system('clear')
        tprint(titulo)
        print(erro_valor)
        sleep(5)
        os.system('clear')
    except TypeError:
        os.system('clear')
        tprint(titulo)
        print(erro_type)
        sleep(5)        
        os.system('clear')
    except IndexError:
        os.system('clear')
        tprint(titulo)
        print(erro_index)
        sleep(5)
        os.system('clear')
    except KeyError:
        os.system('clear')
        tprint(titulo)
        print(erro_key)
        sleep(5)
        os.system('clear')

def menu_pet_view():
    try: 
        tprint(titulo)
        print(menu_pet)
        escolha_usuario_pet = int(input(insert_option_view))
        if escolha_usuario_pet == 1:
            crud_pet()
        if escolha_usuario_pet == 2:
            crud_tutor()
        if escolha_usuario_pet == 3:
           crud_consulta() 
        if escolha_usuario_pet == 4:
            busca_nome = str(input(nome_pet))
            pet.see_infos_pet(busca_nome)
            escolha_id = str(input(id_pet))
            anamenase = str(input())
            pet.register_anamenase(escolha_id, anamenase)
        if escolha_usuario_pet == 5:
            escolha_view = 1
            busca_nome = str(input(nome_pet))
            pet.see_infos_pet(busca_nome)
            while escolha_view == 1:
                escolha_view = (str(input(return_men)))
        if escolha_usuario_pet == 6:
            med_pet()
        if escolha_usuario_pet == 0:
            os.system('clear')
    except ValueError:
        os.system('clear')
        tprint(titulo)
        print(erro_valor)
        sleep(5)
        os.system('clear')
    except TypeError:
        os.system('clear')
        tprint(titulo)
        print(erro_type)
        sleep(5)
        os.system('clear')
    except IndexError:
        os.system('clear')
        tprint(titulo)
        print(erro_index)
        sleep(5)
        os.system('clear')
    except KeyError:
        os.system('clear')
        tprint(titulo)
        print(erro_key)
        sleep(5)
        os.system('clear')

def med_pet():
    busca_nome = str(input(nome_pet))
    pet.see_infos_pet(busca_nome)
    escolha_id = str(input(id_pet))
    medicacao = str(input())
    quantidade = float(input())
    prescricao = {}
    prescricao[medicacao] = quantidade
    while True:
        print(add_mais_medicamento)
        escolha = int(input())
        if escolha == 1:
            medicacao = str(input())
            quantidade = float(input())
            prescricao = {}
            prescricao[medicacao] = quantidade
        else:
            break
    pet.create_recipe(escolha_id, prescricao)

def menu_tutor_view():
    try:
        tprint(titulo)
        print(menu_vet)
        escolha_vet = int(input())
        if escolha_vet == 1:
            busca_nome = str(input(nome_pet))
            pet.see_infos_pet(busca_nome)
            escolha_id = str(input(id_pet))
            vet.check_consult_date(escolha_id)
            escolha_vet = int(input(return_men))
        if escolha_vet == 2:
            busca_nome = str(input(nome_pet))
            pet.see_infos_pet(busca_nome)
            escolha_id = str(input(id_pet))
            vet.remenber_consult(escolha_id)
            escolha_vet = int(input(return_men))
        if escolha_vet == 0:
            os.system('clear')
    except ValueError:
        os.system('clear')
        tprint(titulo)
        print(erro_valor)
        sleep(5)
        os.system('clear')
    except TypeError:
        os.system('clear')
        tprint(titulo)
        print(erro_type)
        sleep(5)
        os.system('clear')
    except IndexError:
        os.system('clear')
        tprint(titulo)
        print(erro_index)
        sleep(5)
        os.system('clear')
    except KeyError:
        os.system('clear')
        tprint(titulo)
        print(erro_key)
        sleep(5)
        os.system('clear')

def view():
    check_database()
    while True:
        try:
            os.system('clear')
            tprint(titulo)
            print(menu_inicial)
            escolha_usuario = int(input(insert_option_view))
            os.system('clear')
            if escolha_usuario == 1:
                menu_pet_view()
            if escolha_usuario == 2:
                menu_tutor_view()
            if escolha_usuario == 0:
                break
        except ValueError:
            os.system('clear')
            tprint(titulo)
            print(erro_valor)
            sleep(5)
            os.system('clear')
        except TypeError:
            os.system('clear')
            tprint(titulo)
            print(erro_type)
            sleep(5)        
            os.system('clear')
        except IndexError:
            os.system('clear')
            tprint(titulo)
            print(erro_index)
            sleep(5)
            os.system('clear')
        except KeyError:
            os.system('clear')
            tprint(titulo)
            print(erro_key)
            sleep(5)
            os.system('clear')
view()
