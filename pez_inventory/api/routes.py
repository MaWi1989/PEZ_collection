from flask import Blueprint, request, jsonify
from pez_inventory.helpers import token_required
from pez_inventory.models import db,User

api = Blueprint('api', __name__, url_prefix = '/api')

# @api.route('/getdata')
# @token_required
# def getdata(current_user_token):
#     return {'some': 'value'}

