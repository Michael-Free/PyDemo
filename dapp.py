"""
Decentralized Application
"""
# Flask requirements
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired

# DAPP Requirements
from hexbytes import HexBytes
from web3.auto import w3
from deploycontract import ASSETREGISTER

APP = Flask(__name__)
BOOTSTRAP = Bootstrap(APP)
APP.config['SECRET_KEY'] = 'TempSecretKey'

# Registration Form for the application
class RegisterForm(FlaskForm):
    """
    Drop down form field for choosing the ethereum address.
    SelectField specifies that this will be a drop down field.
    'Ethereum Address' is the label we'll give to this drop down field
    # A text input field for the form.
    """
    ethereum_address = SelectField('Ethereum Address', choices=[])
    some_string = StringField('Some String', [InputRequired()])

# Application routes
@APP.route("/")
def home():
    """
    return the home.html template
    Pass the contract address to the home.html template
    """
    return render_template(
        'home.html',
        contractaddress=ASSETREGISTER.address
    )

@APP.route("/register", methods=['GET'])
def register():
    """
    # Calling the registration form class
    # List personal accounts.
    # Using n+1 to number each ethereum account
    # return the register.html template
    # pass the register form to the register.html template
    # pass the contract address to the register.html template
    """
    form = RegisterForm()
    form.ethereum_address.choices = []
    minus_one = -1
    for chooseaccount in w3.personal.listAccounts:
        minus_one = minus_one+1
        form.ethereum_address.choices += [(minus_one, chooseaccount)]
    return render_template(
        'register.html',
        registerform=form,
        contractaddress=ASSETREGISTER.address
    )

@APP.route("/registered", methods=['POST'])
def registered():
    """
    Calling a contract function and interact with it using the data from the input
    provided previously.
    """
    call_contract_function = ASSETREGISTER.functions.setRegistration(
        request.form['some_string'],
        w3.eth.accounts[int(request.form['ethereum_address'])]).transact() # create the transaction
    transaction_info = w3.eth.getTransaction(call_contract_function)
    return render_template(
        'registered.html',
        # pass these variables to the html template
        reg_ethaddress=w3.eth.accounts[int(request.form['ethereum_address'])],
        reg_serial=request.form['some_string'],
        reg_accountnumber=request.form['ethereum_address'],
        reg_receipt=w3.eth.getTransactionReceipt(call_contract_function),
        reg_txhash=HexBytes.hex(transaction_info['hash']),
        reg_txdata=HexBytes(transaction_info['input']),
        contractaddress=ASSETREGISTER.address
    )

# Wrapper
if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=5000)
