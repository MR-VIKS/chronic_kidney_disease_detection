from flask import Blueprint, render_template, request
from app.ml_model import kidney_model

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    """Educational Dashboard Landing Page"""
    return render_template('index.html')

@main_bp.route('/check', methods=['GET'])
def check():
    """Form to accept patient inputs for CKD evaluation"""
    return render_template('check.html')

@main_bp.route('/predict', methods=['POST'])
def predict():
    """Processing route for form submissions"""
    if request.method == 'POST':
        sg = float(request.form['sg'])
        htn = float(request.form['htn'])
        hemo = float(request.form['hemo'])
        dm = float(request.form['dm'])
        al = float(request.form['al'])
        appet = float(request.form['appet'])
        rc = float(request.form['rc'])
        pc = float(request.form['pc'])

        # Order matches input features defined in previously existing app.py: 
        # sg, htn, hemo, dm, al, appet, rc, pc
        input_data = [sg, htn, hemo, dm, al, appet, rc, pc]
        prediction = kidney_model.predict(input_data)

        return render_template('result.html', prediction=prediction)
