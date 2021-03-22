from flask import render_template, request
from flask.helpers import flash, url_for
from flask_login import current_user, login_user, logout_user, login_required
import flask_login

import matplotlib
from werkzeug.utils import redirect
matplotlib.use('Agg') # Prevents flask from running outside of main thread. Recommended in MPL docu

from werkzeug.urls import url_parse

import matplotlib.pyplot as plt

from app import app, db
from app.models import DiagnosisData, User
from app.forms import InputDiagnosisData, LoginForm, RegistrationForm
from app.parse import GenerateGraphs, MachineLearning


@app.route('/')
@app.route('/index')
def index():
    #GenerateGraphs.graphs() # Generates graph


    # 'graph1' is malignant / 'graph2' is benign.
    # Couldn't work out how to determine which graph is which based of diagnosis
    url_graph1 = 'static/images/graph1.png'
    url_graph2 = 'static/images/graph2.png'


    return render_template('index.html', title = "Hackathon", url_1 = url_graph1, url_2 = url_graph2)


@app.route('/diagnosis', methods = ['GET', 'POST'])
@login_required
def diagnose():
    form = InputDiagnosisData()

    if request.method == 'POST':
        if form.validate_on_submit():

            # Had to individually store each form param into the list 
            # as the alternative was workable.
            newList = []
            newList.append(form.radius_mean.data)
            newList.append(form.texture_mean.data)
            newList.append(form.perimeter_mean.data)
            newList.append(form.area_mean.data)
            newList.append(form.smoothness_mean.data)
            newList.append(form.compactness_mean.data)
            newList.append(form.concavity_mean.data)
            newList.append(form.concave_points_mean.data)
            newList.append(form.symmetry_mean.data)
            newList.append(form.fractal_dimension_mean.data)
            newList.append(form.radius_se.data)
            newList.append(form.texture_se.data)
            newList.append(form.perimeter_se.data)
            newList.append(form.area_se.data)
            newList.append(form.smoothness_se.data)
            newList.append(form.compactness_se.data)
            newList.append(form.concavity_se.data)
            newList.append(form.concave_points_se.data)
            newList.append(form.symmetry_se.data)
            newList.append(form.fractal_dimension_se.data)
            newList.append(form.radius_worst.data)
            newList.append(form.texture_worst.data)
            newList.append(form.perimeter_worst.data)
            newList.append(form.area_worst.data)
            newList.append(form.smoothness_worst.data)
            newList.append(form.compactness_worst.data)
            newList.append(form.concavity_worst.data)
            newList.append(form.concave_points_worst.data)
            newList.append(form.symmetry_worst.data)
            newList.append(form.fractal_dimension_worst.data)

            # Then had to convert said list above into a mess of a 
            # nested list without the float precision as the ML is picky
            dataset = [[]]
            dataset = [[float(n) for n in newList]]

            predictedDiagnosis = MachineLearning.returnPrediction(dataset)

            # Finally the dataset gets stored to the DB along with the predicted
            # diagnosis from the ML algo 
            new_Diagnosis = DiagnosisData(        
                diagnosis = predictedDiagnosis[0],
                radius_mean = form.radius_mean.data,
                texture_mean = form.texture_mean.data,
                perimeter_mean = form.perimeter_mean.data,
                area_mean = form.area_mean.data,
                smoothness_mean = form.smoothness_mean.data,
                compactness_mean = form.compactness_mean.data,
                concavity_mean = form.concavity_mean.data,
                concave_points_mean = form.concave_points_mean.data,
                symmetry_mean = form.symmetry_mean.data,
                fractal_dimension_mean = form.fractal_dimension_mean.data,
                radius_se = form.radius_se.data,
                texture_se = form.texture_se.data,
                perimeter_se = form.perimeter_se.data,
                area_se = form.area_se.data,
                smoothness_se = form.smoothness_se.data,
                compactness_se = form.compactness_se.data,
                concavity_se = form.concavity_se.data,
                concave_points_se = form.concave_points_se.data,
                symmetry_se = form.symmetry_se.data,
                fractal_dimension_se = form.fractal_dimension_se.data,
                radius_worst = form.radius_worst.data,
                texture_worst = form.texture_worst.data,
                perimeter_worst = form.perimeter_worst.data,
                area_worst = form.area_worst.data,
                smoothness_worst = form.smoothness_worst.data,
                compactness_worst = form.compactness_worst.data,
                concavity_worst = form.concavity_worst.data,
                concave_points_worst = form.concave_points_worst.data,
                symmetry_worst = form.symmetry_worst.data,
                fractal_dimension_worst = form.fractal_dimension_worst.data)

            db.session.add(new_Diagnosis)
            db.session.commit() # finally commits the dataset along with predicted diag to DB

            userDiag = ""
            if predictedDiagnosis[0] == 'B':
                userDiag = "Benign"
            else:
                userDiag = 'Malignant'

            flash("Your predicted diagnosis is: " + userDiag)

            return redirect(url_for('index'))


    return render_template('diagnosis.jinja', title = "Get Diagnosis", form = form)


@app.route('/mlAccuracy')
def mlAccuracy():
    table = MachineLearning.getMLAccuracy()
    table = table.to_html()

    return render_template('mlAccuracy.jinja', title = "Accuracy of Machine Learning Algorithm", table = table)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        login_user(user)
        return redirect(url_for('index'))

    return render_template('login.jinja', title = 'Sign in', form = form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flask_login.login_user(user)
        return redirect(url_for('index'))
    return render_template('register.jinja', title = 'Register', form = form)