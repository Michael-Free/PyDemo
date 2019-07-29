# OS/APP Requirements
import json
import os.path

# Flask requirements
from flask import Flask, render_template, jsonify, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectField, validators
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug import secure_filename
from wtforms.validators import InputRequired

# DAPP Requirements
from hexbytes import HexBytes
from web3.auto import w3
from deploycontract import assetregister, StorageContract

app = Flask(__name__)
bootstrap = Bootstrap(app)
dir_path = os.path.dirname(os.path.realpath(__file__))
app.config['SECRET_KEY'] ='TempSecretKey'

# Forms to fill out for the app
class RegisterForm(FlaskForm):
    ethaddress = SelectField('Ethereum Address', choices=[])
    serialnumber = StringField('Serial Number', [InputRequired()])
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg','jpeg','png'], 'Images only!')
    ])
class ReportForm(FlaskForm):
    ethaddress = SelectField('Ethereum Address', choices=[])
    serialnumber = StringField('Serial Number', [InputRequired()])
    location = StringField('Location', [InputRequired()])

# Application routes
@app.route("/")
def home():
    return render_template('home.html', contractaddress=assetregister.address)

@app.route("/register", methods=['GET'])
def register():
    form = RegisterForm()
    form.ethaddress.choices = []
    n = -1
    # LIST PERSONAL ACCOUNTS
    for chooseaccount in w3.personal.listAccounts:
        n = n+1
        form.ethaddress.choices += [(n, chooseaccount)]
    return render_template('register.html', registerform=form, contractaddress=assetregister.address)

@app.route("/registered", methods=['POST'])
def registered():
    rec_contractaddress = assetregister.address
    rec_ethaddress = w3.eth.accounts[int(request.form['ethaddress'])]
    rec_accountnumber = request.form['ethaddress']
    rec_serial = request.form['serialnumber']
    if 'photo' in request.files:
        photo = request.files['photo']
        upload_path = str(dir_path)+'/upload'
        if photo.filename != '':
            photo.save(os.path.join(upload_path, photo.filename))
            #upload_ipfs = ipfs.add(str(upload_path)+'/'+bikephoto.filename) 
            #ipfs_img_hash = json.loads(str(json.dumps(upload_ipfs)))
            #print(ipfs_img_hash['Hash'])
    registered = assetregister.functions.setRegistration(rec_serial, rec_ethaddress).transact()
    register_receipt = w3.eth.getTransactionReceipt(registered)
    return render_template('registered.html', reg_photo="form.photo.data", reg_ethaddress=rec_ethaddress, reg_serial=rec_serial, contractaddress=assetregister.address)


# Wrapper
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
