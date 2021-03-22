from flask import render_template, request
from flask.helpers import url_for

import matplotlib
from werkzeug.utils import redirect
matplotlib.use('Agg') # Prevents flask from running outside of main thread. Recommended in MPL docu

import matplotlib.pyplot as plt

from app import app, db
from app.models import DiagnosisData
from app.forms import InputDiagnosisData
from app.parse import GenerateGraphs, MachineLearning


@app.route('/')
@app.route('/index')
def index():
    #GenerateGraphs.graphs() # Generates graph


    # 'graph1' is malignant / 'graph2' is benign.
    # Couldn't work out how to determine which graph is which based of diagnosis
    url_graph1 = 'static/images/graph1.png'
    url_graph2 = 'static/images/graph2.png'


    return render_template('index.jinja', title = "Hackathon", url_1 = url_graph1, url_2 = url_graph2)


@app.route('/Diagnosis', methods = ['GET', 'POST'])
def diagnose():
    form = InputDiagnosisData()

    if request.method == 'POST':
        if form.validate_on_submit():
            new_Diagnosis = DiagnosisData(            
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
            fractal_dimension_worst = form.fractal_dimension_worst.data,
            diagnosis = form.diagnosis.data)


            db.session.add(new_Diagnosis)
            db.session.commit()

            return redirect(url_for('index'))


    return render_template('diagnosis.jinja', title = "Get Diagnosis", form = form)


@app.route('/mlAccuracy')
def mlAccuracy():
    table = MachineLearning.getMLAccuracy()
    table = table.to_html()


    return render_template('mlAccuracy.jinja', title = "Accuracy of Machine Learning Algorithm", table = table)