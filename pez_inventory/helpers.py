from functools import wraps

import secrets
import decimal
import requests

from flask import request, jsonify, json

from pez_inventory.models import User

def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split(' ')[1]
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            current_user_token = User.query.filter_by(token = token).first()
            print(token)
        except:
            owner = User.query.filter_by(token = token).first()

            if token != owner.token and secrets.compare_digest(token, owner.token):
                return jsonify({'message':'Token is invalid'})
        return our_flask_function(current_user_token, *args, **kwargs)
    return decorated




class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super(JSONEncoder,self).default(obj)



def random_fact_generator():
    url = "https://facts-by-api-ninjas.p.rapidapi.com/v1/facts"

    headers = {
	"X-RapidAPI-Key": "9b16110cdemsh97cefceb253d517p1e1aecjsn9ef744f7b15e",
	"X-RapidAPI-Host": "facts-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    fact = response.json()

    return fact[0]['fact']


