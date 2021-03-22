from app import db, login, app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class DiagnosisData(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    diagnosis = db.Column(db.String(10), index = True, unique = False)
    radius_mean = db.Column(db.Float, index = True, unique = False)
    texture_mean = db.Column(db.Float, index = True, unique = False)
    perimeter_mean = db.Column(db.Float, index = True, unique = False)
    area_mean = db.Column(db.Float, index = True, unique = False)
    smoothness_mean = db.Column(db.Float, index = True, unique = False)
    compactness_mean = db.Column(db.Float, index = True, unique = False)
    concavity_mean = db.Column(db.Float, index = True, unique = False)
    concave_points_mean = db.Column(db.Float, index = True, unique = False)
    symmetry_mean = db.Column(db.Float, index = True, unique = False)
    fractal_dimension_mean = db.Column(db.Float, index = True, unique = False)
    radius_se = db.Column(db.Float, index = True, unique = False)
    texture_se = db.Column(db.Float, index = True, unique = False)
    perimeter_se = db.Column(db.Float, index = True, unique = False)
    area_se = db.Column(db.Float, index = True, unique = False)
    smoothness_se = db.Column(db.Float, index = True, unique = False)
    compactness_se = db.Column(db.Float, index = True, unique = False)
    concavity_se = db.Column(db.Float, index = True, unique = False)
    concave_points_se = db.Column(db.Float, index = True, unique = False)
    symmetry_se = db.Column(db.Float, index = True, unique = False)
    fractal_dimension_se = db.Column(db.Float, index = True, unique = False)
    radius_worst = db.Column(db.Float, index = True, unique = False)
    texture_worst = db.Column(db.Float, index = True, unique = False)
    perimeter_worst = db.Column(db.Float, index = True, unique = False)
    area_worst = db.Column(db.Float, index = True, unique = False)
    smoothness_worst = db.Column(db.Float, index = True, unique = False)
    compactness_worst = db.Column(db.Float, index = True, unique = False)
    concavity_worst = db.Column(db.Float, index = True, unique = False)
    concave_points_worst = db.Column(db.Float, index = True, unique = False)
    symmetry_worst = db.Column(db.Float, index = True, unique = False)
    fractal_dimension_worst = db.Column(db.Float, index = True, unique = False)

    def __repr__(self):
        return "<ID: {} | Diagnosis: {}".format(self.id, self.diagnosis)


# Class instantiating users
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    

    def __repr__(self):
        return '<User {}>'.format(self.username)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



@login.user_loader
def load_user(id):
    return User.query.get(int(id))