'''Criando e recuprando dados em um banco de dados SQL, utilizando ORM'''

from sqlalchemy import (
    Integer,
    String,
    Column,
    ForeignKey,
    select,
    create_engine,
)

from sqlalchemy.orm import (
    Session,
    declarative_base,
    relationship,
)

Base = declarative_base()

class Client(Base):
    ''' Criando a Tabela client'''
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=False)

    account = relationship(
        'Account', back_populates='client'
    )

    def __repr__(self):
        return f'''
        Cliente: {self.name}
        ID: {self.id}
        CPF: {self.cpf}
        Address: {self.address}'''


class Account(Base):
    ''' Criando a Tabela account'''
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    type = Column(String, default='Conta-Corrente')
    branch = Column(String, default='0001')
    num = Column(String, unique=True, nullable=False)
    id_client = Column(Integer, ForeignKey('client.id'), unique=True)

    client = relationship(
        'Client', back_populates='account'
    )

    def __repr__(self):
        return f'''
    Conta: {self.num}
    ID: {self.id}
    Client ID: {self.id_client}
    Type: {self.type}
    Branch: {self.branch}'''


engine = create_engine('sqlite://')

Base.metadata.create_all(engine)


Bruno = Client(
    name = 'Bruno',
    cpf = '123.123.123-00',
    address = 'Av. Taltaltal, 00',
    account = [Account(
        type = 'Conta-Corrente',
        num = 1
    )]
)

Mariana = Client(
    name = 'Mariana',
    cpf = '123.123.123-11',
    address = 'Rua Taltaltal, 00',
    account = [Account(
        type = 'Special Account',
        num = 2
    )]
)
data_list_to_add = [Bruno, Mariana]

connection = engine.connect()

with Session(engine) as session:
    session.add_all(data_list_to_add)
    session.commit()
    session.close()


def search_by_cpf(cpf_number):
    ''' Função para procurar no banco de dados o cliente com o CPF especificado
    params:
        cpf_number: CPF a ser procurado
    return: 
        Retorna dos dados persistidos no banco de dados da pessoa cujo CPF foi especificado
    '''
    stmt = select(Client).where(Client.cpf.in_([cpf_number]))
    find_client = [
        result for result in session.scalars(stmt)
    ]
    if find_client:
        return find_client[0]
    return f'@@@@ Nenhum Cliente foi encontrando com o CPF: {cpf_number}'

print(search_by_cpf('123.123.123-00'))

def search_by_account_num(account_num):
    ''' Função para procurar no banco de dados o cliente com o numero da conta especificado
    params:
        account_num: Numero da Conta a ser procurado

    return: Retorna os dados do Cliente e da Conta do numero da conta especificado.
    
    '''
    join_stmt = (select(Client.name, Client.cpf, Client.address,
                         Account.type, Account.branch, Account.num, Account.id_client)
                 .join_from(Account, Client)
                 .where(Account.num.in_([account_num])))

    find_client = [
        result for result in connection.execute(join_stmt)
    ]
    name, cpf, address, type_account, branch, num, client_id = find_client[0]
    if find_client:
        return f'''
    Conta: {num}
    Client ID: {client_id}
    Type: {type_account}
    Branch: {branch}

    Detalhes do Cliente: {name}
    CPF: {cpf}
    Address: {address}
'''
    return f'@@@@ Nenhuma conta com o número {account_num} foi encontrada! @@@@'

print(search_by_account_num(2))
