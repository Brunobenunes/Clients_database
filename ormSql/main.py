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
    declarative_base,
    relationship
)

Base = declarative_base()

class Client(Base):
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


