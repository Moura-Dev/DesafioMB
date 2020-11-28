import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine,Column, Integer, String, ForeignKey
from sqlalchemy import text


Base = declarative_base()

class FeirasLivres(Base):

    __tablename__ = "feiras_livres"
    id = Column('id',Integer, primary_key=True)
    long_ = Column('long_',String)
    lat = Column('lat',String)
    setcens = Column('setcens',String)
    areap = Column('areap',String)
    coddist = Column('coddist',String)
    distrito = Column('distrito',String)
    codsubprefe = Column('codsubprefe',String)
    subprefe = Column('subprefe',String)
    regiao5 = Column('regiao5',String)
    regiao8 = Column('regiao8',String)
    nome_feira = Column('nome_feira',String)
    registro = Column('registro',String)
    logradouro = Column('logradouro',String)
    numero = Column('numero',String)
    bairro = Column('bairro',String)
    referencia = Column('referencia',String)

engine = create_engine('mysql+mysqldb://moura:itnisan19@localhost/api')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)
session = Session()


feiraslivres = FeirasLivres()
feiraslivres.id = 1000000
feiraslivres.long_ = 119393
feiraslivres.lat = 103939
feiraslivres.setcens = 1919
feiraslivres.areap = 19191
feiraslivres.coddist = 55
feiraslivres.distrito = "Sao paulo distrito"
feiraslivres.codsubprefe = "subprefeitura"
feiraslivres.subprefe = "55"
feiraslivres.regiao5 = "333"
feiraslivres.regiao8 = 111
feiraslivres.registro = 193
feiraslivres.logradouro = "rua anchieta"
feiraslivres.numero = 210
feiraslivres.bairro = "jardim dom bosco"
feiraslivres.referencia = "transamerica"

session.add(feiraslivres)
session.commit()

session.close()







# feiras = ('id', 'long_', 'lat', 'setcens', 'areap', 'coddist', 'distrito', 'codsubprefe', 'subprefe','regiao5', 'regiao8', 'nome_feira', 'registro', 'logradouro', 'numero', 'bairro', 'referencia')

# with open("data/DEINFO_AB_FEIRASLIVRES_2014.csv", "r") as data:
#     valores = []
#     contador = 0
#     lis = []
#     for line in data:
#         for item in line.split(','):
#             if contador > 16:
#                 contador = 0
#             valores.append(item)
#              #FeirasLivres[contador]
#             lis.append({feiras[contador] : item})
#             contador += 1
#         #session.add(lis)
#         #session.commit()
#             #print(item)
#         print(lis)
#         #session.add(newfeira)
        

#         #print(valores)
#         valores.clear()




        


#ID,LONG,LAT,SETCENS,AREAP,CODDIST,DISTRITO,CODSUBPREF,SUBPREFE,REGIAO5,REGIAO8,NOME_FEIRA,REGISTRO,LOGRADOURO,NUMERO,BAIRRO,REFERENCIA
#23,-46625498,-23501502,355030870000005,3550308005064,71,SANTANA,5,SANTANA-TUCURUVI,Norte,Norte 2,SANTANA,4015-0,RUA GABRIEL PIZZA,S/N,SANTANA,DR.ZUQUIM