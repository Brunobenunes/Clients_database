''' Recuperação de dados NOSQL com pymongo'''

import pymongo

client = pymongo.MongoClient(
    'mongodb+srv://BBpymongoDiO:dio123abc@bankclients.2mxjxjz.mongodb.net/'
    '?retryWrites=true&w=majority'
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

def search_by_account_number(account_number):
    '''Função de procura no banco de dados o cliente que possui a conta com o numero especificado
        params:
            account_number: Numero da Conta a ser procurada
        return:
            Retorna os dados do Cliente, juntando com os dados da Conta'''
    find_client = clients_list.find_one({'accounts.num': account_number})
    if find_client:
        find_account = [
        account for account in find_client['accounts'] if account['num'] == account_number
        ][0]
        return print(f'''
        Cliente: {find_client['name']}
        CPF: {find_client['cpf']}
        Address: {find_client['address']}

        Detalhes da Conta:
        Numero da Conta: {find_account['num']}
        Branch: {find_account['branch']} ''')
    return print(f'@@@@ Nenhuma conta com o número {account_number} foi econtrada! @@@@')

search_by_account_number('2')
