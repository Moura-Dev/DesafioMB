import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import text

#from models import FeirasLivres

engine = create_engine('mysql+mysqldb://moura:itnisan19@localhost/api')
Session = sessionmaker(bind=engine)
session = Session()

# t = text("SELECT * FROM feiras_livres")
# result = session.execute(t)
# for a in result:
#     print(a)


feiras = ('id', 'long_', 'lat', 'setcens', 'areap', 'coddist', 'distrito', 'codsubprefe', 'subprefe','regiao5', 'regiao8', 'nome_feira', 'registro', 'logradouro', 'numero', 'bairro', 'referencia')

with open("data/DEINFO_AB_FEIRASLIVRES_2014.csv", "r") as data:
    valores = []
    contador = 0
    lis = []
    for line in data:
        for item in line.split(','):
            if contador > 16:
                contador = 0
            valores.append(item)
             #FeirasLivres[contador]
            lis.append({feiras[contador] : item})
            contador += 1
        session.add(lis)
        session.commit()
            #print(item)
        print(lis)
        #session.add(newfeira)
        

        #print(valores)
        valores.clear()




        


#ID,LONG,LAT,SETCENS,AREAP,CODDIST,DISTRITO,CODSUBPREF,SUBPREFE,REGIAO5,REGIAO8,NOME_FEIRA,REGISTRO,LOGRADOURO,NUMERO,BAIRRO,REFERENCIA
#23,-46625498,-23501502,355030870000005,3550308005064,71,SANTANA,5,SANTANA-TUCURUVI,Norte,Norte 2,SANTANA,4015-0,RUA GABRIEL PIZZA,S/N,SANTANA,DR.ZUQUIM