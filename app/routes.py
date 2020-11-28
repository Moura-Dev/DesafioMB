from .views import testando
from flask import Blueprint, jsonify, request
from . import db
from .models import FeirasLivres


main = Blueprint('main', __name__)


@main.route('/')
def teste():
    return testando()

