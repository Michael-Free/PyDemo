
# Flask requirements
from flask import Flask, render_template, jsonify, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectField, validators
from wtforms.validators import InputRequired

# DAPP Requirements
from hexbytes import HexBytes
from web3.auto import w3
from deploycontract import assetregister, StorageContract

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] ='TempSecretKey'

# Registration Form for the application
class RegisterForm(FlaskForm):
    # Drop down form field for choosing the ethereum address.
    # SelectField specifies that this will be a drop down field.
    # 'Ethereum Address' is the label we'll give to this drop down field

    ethaddress = SelectField('Ethereum Address', choices=[])
    # A text input field for the form.
    serialnumber = StringField('Serial Number', [InputRequired()])

# Application routes
@app.route("/")
def home():
    # return the home.html template
    return render_template(
        'home.html',
         # Pass the contract address to the home.html template
         contractaddress=assetregister.address
    )

@app.route("/register", methods=['GET'])
def register():
    # Calling the registration form class
    form = RegisterForm()
    form.ethaddress.choices = []
    n = -1
    # List personal accounts.
    for chooseaccount in w3.personal.listAccounts:
        # Using n+1 to number each ethereum account
        n = n+1
        form.ethaddress.choices += [(n, chooseaccount)]
    # return the register.html template
    return render_template(
        'register.html',
        # pass the register form to the register.html template
        registerform=form,
        # pass the contract address to the register.html template
        contractaddress=assetregister.address
    )

@app.route("/registered", methods=['POST'])
def registered():
    # calling the setRegistration function in the smart contract
    registered = assetregister.functions.setRegistration(
        # Pass the serial number from the registration form to the contract function
        request.form['serialnumber'],
        # Pass the chosen ethereum address to the smart contract and use that to send eth from
        w3.eth.accounts[int(request.form['ethaddress'])]).transact() # create the transaction
    # Get the transaction
    tx =  w3.eth.getTransaction(registered)
    # Get the transaction hash 
    tx_hash = HexBytes.hex(tx['hash'])
    # Get the data sent from the transaction
    tx_data = HexBytes(tx['input'])
    # return the registered.html template
    return render_template(
        'registered.html',
        # pass the ethereum address chosen in /register to the registered.html template
        reg_ethaddress=w3.eth.accounts[int(request.form['ethaddress'])],
        # pass the serial number used in /register to the registered.html template
        reg_serial=request.form['serialnumber'],
        # pass the account number (n+1) to the template
        reg_accountnumber=request.form['ethaddress'],
        # pass the transaction receipt on to the template
        reg_receipt=w3.eth.getTransactionReceipt(registered),
        # pass the transaction hash to the template
        reg_txhash= tx_hash,
        # Pass the transaction data (inputs) to the template
        reg_txdata= tx_data,
        # Pass the contract address to the template
        contractaddress=assetregister.address
    )

# Wrapper
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
