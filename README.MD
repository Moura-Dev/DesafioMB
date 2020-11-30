

# APi-FLASK-PYTHON
Desafio MercadoBitcoin :

# Crie um virtualenv 
python3 -m virtualenv venv

# Ative virtualenv
source /venv/bin/activate

# Dependencias para usar o sistema
pip install -r requirements.txt

# Exportar flask:
Export FLASK_APP=app

# Conectar Banco de Dados
Edit app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/api' no arquivo __init__.py com suas configuraçoes



# Executando Script Para Criar Banco de Dados e Inserir Dados no Banco de Dados
python3 script/rotina.py
 


# Executando teste 
python -m unittest 


#Ligando Api

Execute no terminal o Comando Flask run


# Endpoint Consultar Feiras (Listar todas as Feiras no banco):

Method: Get
url =  /feira/ (GET)


# Endpoint POST Feira :

Method: POST

url = /feira/ (POST)

modelo de url = Feira


 {
        "areap": "3550308005145",
        "bairro": "VL NOVA atualizada",
        "coddist": "60",
        "codsubprefe": "21",
        "distrito": "PENHA",
        "lat": "-23520880",
        "logradouro": "RUA FRANCISCO DE OLIVEIRA BRAGA",
        "long_": "-46513450",
        "nome_feira": "VILA NOVA",
        "numero": "13.000000",
        "referencia": "RUA OLIVIA DE OLIVEIRA",
        "regiao5": "Leste",
        "regiao8": "Leste 1",
        "registro": "3048-1",
        "setcens": "355030859000173",
        "subprefe": "PENHA"
    }




# Endpoint Update Feira pelo campo id:

Method: PUT, PATCH

url = /feira/id/ (Put)

modelo de url = feira/1/


 {
        "areap": "3550308005145",
        "bairro": "VL NOVA atualizada",
        "coddist": "60",
        "codsubprefe": "21",
        "distrito": "PENHA",
        "lat": "-23520880",
        "logradouro": "RUA FRANCISCO DE OLIVEIRA BRAGA",
        "long_": "-46513450",
        "nome_feira": "VILA NOVA",
        "numero": "13.000000",
        "referencia": "RUA OLIVIA DE OLIVEIRA",
        "regiao5": "Leste",
        "regiao8": "Leste 1",
        "registro": "3048-1",
        "setcens": "355030859000173",
        "subprefe": "PENHA"
    }




# Em caso de Sucesso retornará:

{
    "Message": "Feira Atualizada com Sucesso!!"
}




# Endpoint Delete Feira pelo campo id:

Method: PUT, PATCH

url = /feira/id/ (Put)

modelo de url = feira/1/ 



# Em caso de Sucesso retornará:

{
    "Message": "Feira Deletada com Sucesso!!"
}