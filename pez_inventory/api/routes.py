from flask import Blueprint, request, jsonify
from pez_inventory.helpers import token_required, random_fact_generator
from pez_inventory.models import db, PEZ, pez_schema, all_pez_schema

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
@token_required
def getdata(current_user_token):
    return {'some': 'value'}


@api.route('/all_pez', methods = ['POST'])
@token_required
def create_pez(current_user_token):
    name = request.json['name']
    series = request.json['series']
    description = request.json['description']
    price = request.json['price']
    value = request.json['value']
    year_intruduced = request.json['year introduced']
    retired = request.json['retired?']
    original_package = request.json['original package?']
    random_fact = random_fact_generator()
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    pez = PEZ(name, series, description, price, value, year_intruduced, retired, original_package, random_fact, user_token = user_token )

    db.session.add(pez)
    db.session.commit()

    response = pez_schema.dump(pez)
    return jsonify(response)




@api.route('/all_pez', methods = ['GET'])
@token_required
def get_all_pez(current_user_token):
    owner = current_user_token.token
    all_pez = PEZ.query.filter_by(user_token = owner).all()
    response = all_pez_schema.dump(all_pez)
    return jsonify(response)



@api.route('/all_pez/<id>', methods = ['GET'])
@token_required
def get_pez(current_user_token, id):
    if id:
        pez = PEZ.query.get(id)
        response = pez_schema.dump(pez)
        return jsonify(response)
    else:
        return jsonify({"message": "Valid Token Required"}),401



@api.route('/all_pez/<id>', methods = ['POST'])
@token_required
def update_pez(current_user_token,id):
    pez = PEZ.query.get(id)
    pez.name = request.json['name']
    pez.series = request.json['series']
    pez.description = request.json['description']
    pez.price = request.json['price']
    pez.value = request.json['value']
    pez.year_introduced = request.json['year intruduced']
    pez.retired = request.json['retired?']
    pez.original_package = request.json['original package?']
    pez.user_token = current_user_token.token


    db.session.commit()
    response = pez_schema.dump(pez)
    return jsonify(response)



@api.route('/all_pez/<id>', methods = ['DELETE'])
@token_required
def delete_pez(current_user_token, id):
    pez = PEZ.query.get(id)
    db.session.delete(pez)
    db.session.commit()
    response = pez_schema.dump(pez)
    return jsonify(response)
