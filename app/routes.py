from .views import (
    BuscarFeira,
    BuscarPorNomeFeira,
    DeletarFeira,
    AtualizarFeira,
    AdicionarFeira,
)
from flask import Blueprint, jsonify


main = Blueprint("main", __name__)


@main.route("/feira/")
def GetFeira():
    return BuscarFeira()


@main.route("/feira/<cod>")
def GetFeiraDistrito(cod):
    return BuscarPorNomeFeira(cod)


@main.route("/feira/<cod>", methods=["DELETE"])
def DeleteFeira(cod):
    return DeletarFeira(cod)


@main.route("/feira/<cod>", methods=["PUT", "PATCH"])
def AtualizarFeiraLivre(cod):
    return AtualizarFeira(cod)


@main.route("/feira/", methods=["POST"])
def CriarFeira():
    return AdicionarFeira()
