from .views import BuscarFeira, BuscarPorNomeFeira, DeletarFeira, AtualizarFeira, AdicionarFeira, hello
from flask import Blueprint, jsonify, request
from . import db
from .models import FeirasLivres


main = Blueprint('main', __name__)


@main.route('/')
def hellowordl():
    return hello()

@main.route('/feira/')
def GetFeira():
    return BuscarFeira()


@main.route('/feira/<cod>')
def GetFeiraDistrito(cod):
    return BuscarPorNomeFeira(cod)


@main.route('/feira/<cod>/', methods=['DELETE'])
def DeleteFeira(cod):
    return DeletarFeira(cod)


@main.route('/feira/<cod>/', methods=['PUT', 'PATCH'])
def AtualizarFeiraLivre(cod):
    return AtualizarFeira(cod)


@main.route('/feira/', methods=['POST'])
def CriarFeira():
    return AdicionarFeira()


