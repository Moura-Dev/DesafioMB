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

#def LerCsv():
with open("data/DEINFO_AB_FEIRASLIVRES_2014.csv", "r") as data:
    valores = []
    contador = 0
    lis = []
    for line in data:
        if contador > 0:
            for item in line.strip().split(','):
                if contador > 16:
                    contador = 0
                valores.append(item)
            feiraslivres = FeirasLivres()
            feiraslivres.long_ = valores[1]
            feiraslivres.lat = valores[2]
            feiraslivres.setcens = valores[3]
            feiraslivres.areap = valores[4]
            feiraslivres.coddist = valores[5]
            feiraslivres.distrito = valores[6]
            feiraslivres.codsubprefe = valores[7]
            feiraslivres.subprefe = valores[8]
            feiraslivres.regiao5 = valores[9]
            feiraslivres.regiao8 = valores[10]
            feiraslivres.nome_feira = valores[11]
            feiraslivres.registro = valores[12]
            feiraslivres.logradouro = valores[13]
            feiraslivres.numero = valores[14]
            feiraslivres.bairro = valores[15]
            if len(valores) == 17:
                feiraslivres.referencia = valores[16]
            print(valores)

            session.add(feiraslivres)
            session.commit()
            session.close()
            

            valores.clear()
        contador += 1


#LerCsv()



        