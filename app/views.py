from flask import jsonify, request
from .models import FeirasLivres
from . import db


def BuscarFeira():

    consultar = FeirasLivres.query.all()
    feiras = []
    if not consultar:
        return jsonify({'Message': "Não Existe Registros"}), 404


    for f in consultar:
        feiras.append({'id': f.id, 'long_': f.long_, 'lat': f.lat,'setcens': f.setcens, 
        'areap': f.areap, 'coddist': f.coddist,'distrito': f.distrito, 'codsubprefe': f.codsubprefe, 
        'subprefe': f.subprefe,'regiao5': f.regiao5, 'regiao8': f.regiao8, 'nome_feira': f.nome_feira,
        'registro': f.registro,'logradouro': f.logradouro, 'numero': f.numero,
        'bairro': f.bairro, 'referencia': f.referencia})


    return jsonify(feiras), 200

   
def BuscafeiraPorId(cod):
    consultar = FeirasLivres.query.filter(FeirasLivres.id == cod)
    feiras = []
    
    if not consultar:
        return jsonify({'Message': "Não Existe Registros"}), 404


    for f in consultar:

        feiras.append({'id': f.id, 'long_': f.long_, 'lat': f.lat,'setcens': f.setcens, 'areap': f.areap, 
        'coddist': f.coddist,'distrito': f.distrito, 'codsubprefe': f.codsubprefe, 'subprefe': f.subprefe,
        'regiao5': f.regiao5, 'regiao8': f.regiao8, 'nome_feira': f.nome_feira,'registro': f.registro,
        'logradouro': f.logradouro, 'numero': f.numero,'bairro': f.bairro, 'referencia': f.referencia})

        return jsonify(feiras), 200


def DeletarFeira(cod):
    FeirasLivres.query.filter(FeirasLivres.id == cod).delete()
    try:
        db.session.commit()
        return jsonify({'Message': "Feira Deletada com Sucesso!!"}), 201

    except:
        return jsonify({'message': "Erro ao Deletar feira!"}), 404


def AtualizarFeira(cod):
    query = FeirasLivres.query.filter(FeirasLivres.id == cod)
    try:
        query.update(request.json)
        db.session.commit()
        return jsonify({'Message': "Feira Atualizada com Sucesso!!"}), 201

    except:
        return jsonify({'message': "Erro ao Atualizar Feira!!"}), 404


def AdicionarFeira():

    new_fr = request.get_json()

    nova_feira = FeirasLivres(long_=new_fr['long_'], lat=new_fr['lat'],setcens=new_fr['setcens'], 
    areap=new_fr['areap'],coddist=new_fr['coddist'], distrito=new_fr['distrito'],
    codsubprefe=new_fr['codsubprefe'], subprefe=new_fr['subprefe'],regiao5=new_fr['regiao5'], 
    regiao8=new_fr['regiao8'],nome_feira=new_fr['nome_feira'], registro=new_fr['registro'],
    logradouro=new_fr['logradouro'], numero=new_fr['numero'],bairro=new_fr['bairro'], referencia=new_fr['referencia'],)
    
    
    try:
        db.session.add(nova_feira)
        db.session.commit()
        return jsonify({'Message': "Feira Criado com Sucesso!!"}), 201


    except:
        return jsonify({'message': "Erro ao Criar Feira!!"}), 404