''' Recuperação de dados NOSQL com pymongo'''

import pymongo

client = pymongo.MongoClient(
    'mongodb+srv://BBpymongoDiO:dio123abc@bankclients.2mxjxjz.mongodb.net/?retryWrites=true&w=majority'
    )

database = client.clients

clients_list = database.clients_list