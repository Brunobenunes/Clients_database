''' Criando a conexão com o Banco e Criando Collections'''

import pymongo

client = pymongo.MongoClient(
    'mongodb+srv://BBpymongoDiO:dio123abc@bankclients.2mxjxjz.mongodb.net/'
    '?retryWrites=true&w=majority'
)

database = client.clients

clients_list = database.clients_list

data_list_to_add = [
    {
        'name': 'Bruno',
        'cpf': '123.123.123-00',
        'address': 'Av. taltaltal, 000',
        'accounts': [
            {
                'type': 'Conta-Corrente',
                'branch': '0001',
                'num': '1',
            }
        ]
    },
    {
        'name': 'Mariana',
        'cpf': '123.123.123-11',
        'address': 'Rua taltaltaltal, 000',
        'accounts': [
            {
                'type': 'Special Account',
                'branch': '0001',
                'num': '2'
            }
        ]
    }
]