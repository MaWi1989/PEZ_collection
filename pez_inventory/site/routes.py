from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from pez_inventory.forms import PEZForm
from pez_inventory.models import PEZ, db, User 
from pez_inventory.helpers import random_fact_generator

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    print('pezpezpezpezpez')
    return render_template('index.html')


@site.route('/profile', methods= ['GET', 'POST'])
@login_required
def profile():
    my_pez = PEZForm()

    try:
        if request.method == "POST" and my_pez.validate_on_submit():
            print("validated")
            name = my_pez.name.data
            series = my_pez.series.data
            description = my_pez.description.data
            price = my_pez.price.data
            value = my_pez.value.data
            year_introduced = my_pez.year_introduced.data
            retired = my_pez.retired.data
            original_package = my_pez.original_package.data
            if my_pez.random_fact.data:
                random_fact = my_pez.random_fact.data
                user = User.query.filter_by(id = current_user.id).first()         
                user_token = user.token
            else:
                random_fact = random_fact_generator() 
                user = User.query.filter_by(id = current_user.id).first()         
                user_token = user.token
            print(user_token)

            pez = PEZ(name, series, description, price, value, year_introduced, retired, original_package, random_fact, user_token)

            db.session.add(pez)
            db.session.commit()

            return redirect(url_for('site.profile'))
    except:
        raise Exception("PEZ not created, please check your form and try again!")

    current_user_token = current_user.token

    all_pez = PEZ.query.filter_by(user_token=current_user_token)


    return render_template('profile.html', form=my_pez, all_pez= all_pez )


        