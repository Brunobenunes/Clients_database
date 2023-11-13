''' Recuperação de dados NOSQL com pymongo'''

import pymongo

client = pymongo.MongoClient(
    'mongodb+srv://BBpymongoDiO:dio123abc@bankclients.2mxjxjz.mongodb.net/?retryWrites=true&w=majority'
    )

database = client.clients

clients_list = database.clients_list

def search_by_cpf(cpf_number):
    ''' Função que procura um determinado cliente com base no cpf
        params:
            cpf_number: Numero de Cpf a ser procurado
        return:
            Dados do Cliente cujo CPF foi especificado'''
    find_client = clients_list.find_one({'cpf': cpf_number})
    if (find_client):
        return print(f'''
    Cliente: {find_client['name']}
    CPF: {cpf_number}
    Address: {find_client['address']}
''')
    return print(f'@@@@ Nenhum Cliente foi encontrado com o CPF: {cpf_number} @@@@')

# Procurando no Algum Cliente com o CPF informado
search_by_cpf('123.123.123-00')

