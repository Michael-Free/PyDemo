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
    ETHADDRESS = SelectField('Ethereum Address', choices=[])
    SERIALNUMBER = StringField('Serial Number', [InputRequired()])

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
    form.ETHADDRESS.choices = []
    n = -1
    for chooseaccount in w3.personal.listAccounts:
        n = n+1
        form.ETHADDRESS.choices += [(n, chooseaccount)]
    return render_template(
        'register.html',
        registerform=form,
        contractaddress=ASSETREGISTER.address
    )

@APP.route("/registered", methods=['POST'])
def registered():
    """
    # calling the setRegistration function in the smart contract
    # Pass the serial number from the registration form to the contract function
    # Pass the chosen ethereum address to the smart contract and use that to send eth from
    # Get the transaction
    # Get the transaction hash
    # Get the data sent from the transaction
    # return the registered.html template
    # pass the ethereum address chosen in /register to the registered.html template
    # pass the serial number used in /register to the registered.html template
    # pass the transaction receipt on to the template
    # pass the transaction hash to the template
    # Pass the transaction data (inputs) to the template
    # Pass the contract address to the template
    """
    REGISTERED = ASSETREGISTER.functions.setRegistration(
        request.form['SERIALNUMBER'],
        w3.eth.accounts[int(request.form['ETHADDRESS'])]).transact() # create the transaction
    TX = w3.eth.getTransaction(REGISTERED)
    TX_HASH = HexBytes.hex(TX['hash'])
    print('TRANSACTION HASH:')
    print(str(TX_HASH))
    print()
    TX_DATA = HexBytes(TX['input'])
    print('TRANSACTION DATA:')
    print(w3.toHex(TX_DATA))
    return render_template(
        'registered.html',
        reg_ethaddress=w3.eth.accounts[int(request.form['ETHADDRESS'])],
        reg_serial=request.form['SERIALNUMBER'],
        reg_accountnumber=request.form['ETHADDRESS'],
        reg_receipt=w3.eth.getTransactionReceipt(REGISTERED),
        reg_txhash=TX_HASH,
        reg_txdata=TX_DATA,
        contractaddress=ASSETREGISTER.address
    )

# Wrapper
if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=5000)
