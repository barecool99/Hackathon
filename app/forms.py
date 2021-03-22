from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired, InputRequired, ValidationError

DIAGNOSIS_OPTIONS = ['Malignant', 'Benign']

class InputDiagnosisData(FlaskForm):
    radius_mean = DecimalField('Radius Mean', validators = [DataRequired(), InputRequired()])
    texture_mean = DecimalField('Texture Mean', validators = [DataRequired(), InputRequired()])
    perimeter_mean = DecimalField('Perimeter Mean', validators = [DataRequired(), InputRequired()])
    area_mean = DecimalField('Area Mean', validators = [DataRequired(), InputRequired()])
    smoothness_mean = DecimalField('Smoothness Mean', validators = [DataRequired(), InputRequired()])
    compactness_mean = DecimalField('Compactness Mean', validators = [DataRequired(), InputRequired()])
    concavity_mean = DecimalField('Concavity Mean', validators = [DataRequired(), InputRequired()])
    concave_points_mean = DecimalField('Concave Points Mean', validators = [DataRequired(), InputRequired()])
    symmetry_mean = DecimalField('Symmetry Mean', validators = [DataRequired(), InputRequired()])
    fractal_dimension_mean = DecimalField('Fractal Dimension Mean', validators = [DataRequired(), InputRequired()])
    radius_se = DecimalField('Radius SE', validators = [DataRequired(), InputRequired()])
    texture_se = DecimalField('Texture SE', validators = [DataRequired(), InputRequired()])
    perimeter_se = DecimalField('Perimeter SE', validators = [DataRequired(), InputRequired()])
    area_se = DecimalField('Area SE', validators = [DataRequired(), InputRequired()])
    smoothness_se = DecimalField('Smoothness SE', validators = [DataRequired(), InputRequired()])
    compactness_se = DecimalField('Compactness SE', validators = [DataRequired(), InputRequired()])
    concavity_se = DecimalField('Concavity SE', validators = [DataRequired(), InputRequired()])
    concave_points_se = DecimalField('Concave Points SE', validators = [DataRequired(), InputRequired()])
    symmetry_se = DecimalField('Symmetry SE', validators = [DataRequired(), InputRequired()])
    fractal_dimension_se = DecimalField('Fractal Dimension SE', validators = [DataRequired(), InputRequired()])
    radius_worst = DecimalField('Radius Worst', validators = [DataRequired(), InputRequired()])
    texture_worst = DecimalField('Texture Worst', validators = [DataRequired(), InputRequired()])
    perimeter_worst = DecimalField('Perimeter Worst', validators = [DataRequired(), InputRequired()])
    area_worst = DecimalField('Area Worst', validators = [DataRequired(), InputRequired()])
    smoothness_worst = DecimalField('Smoothness Worst', validators = [DataRequired(), InputRequired()])
    compactness_worst = DecimalField('Compactness Worst', validators = [DataRequired(), InputRequired()])
    concavity_worst = DecimalField('Concavity Worst', validators = [DataRequired(), InputRequired()])
    concave_points_worst = DecimalField('Concave Radius Mean', validators = [DataRequired(), InputRequired()])
    symmetry_worst = DecimalField('Radius Mean', validators = [DataRequired(), InputRequired()])
    fractal_dimension_worst = DecimalField('Radius Mean', validators = [DataRequired(), InputRequired()])

    diagnosis = SelectField('Diagnosis Type', choices = DIAGNOSIS_OPTIONS, validators = [DataRequired(), InputRequired()])
    submit = SubmitField('Submit')

    def validateIsDecimal(self, form, field):
        if not isinstance(field.data, float):
            raise ValidationError("Field must be a float")