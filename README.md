<p align="center">
<img src="/media/bitcoinbay-logo-00.jpeg">
</p>


# Building dApps with Python, Flask, Solidity, & Web3.py

## Table of Contents

* [Install Requirements](#install-requirements)
* [Getting Started](#getting-started)
  * [Starting Ganache-CLI](#starting-ganache-cli)
  * [Get Familiar with Web3.py](#get-familiar-with-web3py)
    * [Import the Libraries](#import-the-libraries)
    * [Set Ganache-CLI as the Ethereum Blockchain Provider](#set-ganache-cli-as-the-ethereum-blockchain-provider)
    * [Interacting with Ganache-CLI Through Python with Web3.py](#interacting-with-ganache-gli-through-python-with-web3py)
    * [Get Gase Price](#get-gas-price)
    * [Get Balances](#get-balances)
    * [Create New Account](#create-new-account)
    * [Send ETH to New Account](#send-eth-to-new-account)
    * [More Web3.py Info](#more-web3py-info)
* [Explaining Solidity and Smart Contracts](#explaining-solidity-and-smart-contracts)
  * [Solidity and Solc](#solidity-and-solc)
    * [Solc](#solidity)
    * [LLLC](#lllc)
    * [Solc](#solc)
    * [Py-Solc Library](#py-solc-library)
  * [Building A Contract](#building-a-contract)
    * [Sample Contract](#sample-contract)
    * [Learning More About Solidity](#learning-more-about-solidity)
  * [Deploying Contracts](#deploying-contracts)
    * [Deploying with Inline Solidity Code](#deploying-with-inline-solidity-code)
    * [Deploying with a .sol Solidity Contract](#deploying-with-a-sol-solidity-contract)
    * [Building The Contract Interface](#building-the-contract-interface)
* [Using Flask to Build a dApp](#using-flask-to-build-a-dapp)
  * [Setting Up the Flask Environment](#setting-up-the-flask-environment)
    * [dapp.py](#dapppy)
    * [Application Routing - dapp.py](#application-routing---dapppy)
    * [GET - /](#get---)
    * [GET - /register](#get---register)
    * [POST - /registered](#post---registered)
  * [Templates](#templates)
    * [index.html](#indexhtml)
    * [home.html](#homehtml)
    * [register.html](#registerhtml)
    * [registered.html](#registeredhtml)
  
## Install Requirements

System requirements on Ubuntu Server 18.04 LTS

```
sudo apt install libz3-dev python3-dev python3-pip npm unzip
```

This demo uses Solc 0.4.25.  You can install from below:

```
wget https://github.com/ethereum/solidity/releases/download/v0.4.25/solidity-ubuntu-trusty.zip
sudo unzip solidity-ubuntu-trusty.zip -d /usr/bin/
rm -rvf solidity-ubuntu-trusty.zip
```

Install Ganache - the test ethereum blockchain and pip3 requirements

```
sudo npm install -g ganache-cli
git clone https://github.com/Michael-Free/PyDemo.git
cd PyDemo
sudo pip3 install -r requirements.txt
```

[Back To Top](#table-of-contents)

## Getting Started

### Starting Ganache-CLI

Ganache is an ethereum blockchain emulator. it allows developers to make calls to an ethereum-like blockchain, without having to run a node.

```
ganache-cli
```

Ganache is an ethereum blockchain emulator. it allows developers to make calls to an ethereum-like blockchain, without having to run a node.

When it's started, it will generate 10 ETH Public Key addresses and their corresponding keys.  Each address will have 100 ETH by default.

![Ganache-CLI Startup Information](/media/ganache-cli-00.png)

Other information is displayed like HD Wallet, which can be used to import these accounts into a wallet or other applications (Metamask, Parity, etc).

For the purposes of this demonstration, we wont be going too deep into Gas Limits and Gas Prices.  If you would like to learn more about it, this is probably the most informative explanation: https://blockgeeks.com/guides/ethereum-gas/

[Back To Top](#table-of-contents)

### Get Familiar with Web3.py

Web3 is an API to the Ethereum Blockchain to build applications with.  There are many implementations. The most widely used implementation is Web3.js, which Web3.py is derrived from.  So let's get started with a python terminal: ```python3```

[Back To Top](#table-of-contents)

#### Import the Libraries

```
>>> from web3 import Web3, HTTPProvider
```
[Back To Top](#table-of-contents)

#### Set Ganache-CLI as the Ethereum Blockchain Provider

```
>>> web3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
```

[Back To Top](#table-of-contents)

#### Interacting with Ganache-GLI through Python with Web3.py

Get a list of current Ethereum Addresses:

```
>>> web3.personal.listAccounts
```

![Ganache-CLI Ethereum Addresses in Python3 Terminal](/media/ganache-cli-01.png)

Notice that this lists the ethereum addresses started by ganache-cli. The call from python to Web3.py can be observed from the ganache-cli terminal as well.

![Python Call can be seen in Ganache-cli](/media/ganache-cli-02.png)

[Back To Top](#table-of-contents)

#### Get Gas Price

```
>>> web3.eth.gasPrice
20000000000
```
![Ganache-CLI Get Ethereum Gas Price in Python3 Terminal](/media/ganache-cli-03.png)

#### Get Balances 

```
>>> web3.eth.getBalance('0xC599Ca9376b82651b8e9A2ee741B1b404dc41FF8')
100000000000000000000
```
![Get Ethereum Address Balances from address](/media/ganache-cli-04.png)

[Back To Top](#table-of-contents)

#### Create New Account
```
>>> web3.personal.newAccount('YOURPASSWORD')
'0xE972Dc8a9a0701A98dB8466FC555Bc10150Cd977'
```

A new address is now created.  Check the balance on this account:

```
>>> web3.eth.getBalance('0xE972Dc8a9a0701A98dB8466FC555Bc10150Cd977')
0
```
The address should be zero, unlike the other accounts since this is newly created.

[Back To Top](#table-of-contents)

#### Send ETH to New Account

Send some ETH to the new account:

```
>>> web3.eth.sendTransaction({'to': '0xE972Dc8a9a0701A98dB8466FC555Bc10150Cd977', 
                                    'from': web3.eth.coinbase,
                                    'value': 1000000})
HexBytes('0xdd1ca7444da4498e168954669e3f1381f0a3843c40adaaa8e55d32e07c7c5985')
```
The response is the transaction hash registered on the blockchain.  Here is the output of the transaction in ganache-cli:

![Send ETH to new account](/media/ganache-cli-05.png)

[Back To Top](#table-of-contents)

#### More Web3.py Info

For more information and documentation on web3.py:
https://web3py.readthedocs.io/en/stable/index.html
[Back To Top](#table-of-contents)

## Explaining Solidity and Smart Contracts

Smart Contracts (simply put) are small computer programs.  These programs exist on a common blockchain. When triggered, they are self-executing. The terms of the contract between the contract owner and the recipient are expressed as code. Since Smart Contracts exist on a decentralized blockchain, they permit trusted transactions/agreements to be carried out without any need for a central authority, legal system, or enforcement mechanism.  However, due to the structure and security of this platform, there is little need for intermediaries.

This makes the transactions of a Smart Contract transparent, trustless, traceable, irreversable, and globally redundant.

[Back To Top](#table-of-contents)

### Solidity and Solc

#### Solidity

Solidity is statically typed, contract-oriented, and a high-level language for implementing smart contracts on the Ethereum platform.

Ethereum is by far the most popular platform for Solidity, but other platforms use Solidity, such as:  Hyperledger, Ethereum Classic, Monax, CounterParty (on Bitcoin), and even SWIFT has a proof-of-concept built using Solidity.

[Back To Top](#table-of-contents)

#### LLLC

LLLC, the Lovely Little Language Compiler. This binary will translate Solidity Contracts into a Ethereum-Blockchain executable format.  

[Back To Top](#table-of-contents)

#### Solc

Solc is a binary and commandline interface for the Solidity Compiler (LLLC). 

[Back To Top](#table-of-contents)

#### Py-Solc Library

Python wrapper around the solc Solidity compiler. Here is an integral part of building a python-based dApp. 
[Back To Top](#table-of-contents)

### Building A Contract

#### Sample Contract

```
pragma solidity ^0.4.21;
contract StorageContract {
    /* Define variable owner of the type address */
    string public serialnumber;
    address public assetowner;
    /* create an event for registration - events help return values for the ui. */
    event Registration(
       string serialnumber,
       address assetowner
    );
    /* create a function that uses the 2 variables  */
    function setRegistration (string newSerialnumber, address newAssetowner) public {
        serialnumber = newSerialnumber;
        assetowner = newAssetowner;
        emit Registration(serialnumber, assetowner);
    }
}
```

[Back To Top](#table-of-contents)

#### Learning More About Solidity

There are plenty of online resources for learning more about Solidity.  For exploring more, take a look at some of the provided documentation and sample contract-implementations:
* Solidity Documentation: https://solidity.readthedocs.io/en/v0.4.24/
* OpenZeppelin: https://github.com/OpenZeppelin/openzeppelin-contracts
* BlockGeeks: https://github.com/blockgeeks/workshop/tree/master/src/contracts

[Back To Top](#table-of-contents)

### Deploying Contracts

There are two ways to deploy a contract with Python.  It can be done with the Solidity Contract code written directly inline in a Python application.  It can also be compiled from a ```.sol``` Solidity Contract file.

This section specifically breaks down deploycontract​
384


#### Deploying with Inline Solidity Code

Create a variable for the contract source code.  Create a set of triple quotes, and paste in the contract.

```
CONTRACT_SOURCE_CODE = '''
pragma solidity ^0.4.21;
contract StorageContract {

    /* Define variable owner of the type address */
    string public serialnumber;
    address public assetowner;
    
    /* create an event for registration - events help return values for the ui. */
    event Registration(
       string serialnumber,
       address assetowner
    );
    
    /* create a function that uses the 2 variables  */
    function setRegistration (string newSerialnumber, address newAssetowner) public {
        serialnumber = newSerialnumber;
        assetowner = newAssetowner;
        emit Registration(serialnumber, assetowner);
    }
}
'''
```

Compile the contract:
```
COMPILED_SOL = compile_source(CONTRACT_SOURCE_CODE)
```

[Back To Top](#table-of-contents)

#### Deploying with a .sol Solidity Contract

Create a function to open and read the solidity contract file and compile source:

```
def compile_source_file(file_path):
   with open(file_path, 'r') as f:
      source = f.read()
   return compile_source(source)
```

Create a function to deploy the contract once it has been read and compiled:

```
def deploy_contract(we3, contract_interface):
    tx_hash = we3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']).deploy()
    address = we3.eth.getTransactionReceipt(tx_hash)['contractAddress']
    return address
```

Provide the path to the contract and path:

```
contract_source_path = '/contract/'
compiled_sol = compile_source_file('storage.sol')
```

[Back To Top](#table-of-contents)

#### Building the Contract Interface

```
SMARTCONTRACT_INTERFACE = COMPILED_SOL['<stdin>:StorageContract']
StorageContract = WEB3.eth.contract(
    abi=SMARTCONTRACT_INTERFACE['abi'],
    bytecode=SMARTCONTRACT_INTERFACE['bin'])
```

Setup the transaction to deploy the contract:

```
WEB3.eth.defaultAccount = WEB3.eth.accounts[0]
TX_HASH = StorageContract.constructor().transact()
TX_RECEIPT = WEB3.eth.waitForTransactionReceipt(TX_HASH)
```

Create the Contract Instance:

```
ASSETREGISTER = WEB3.eth.contract(
    address=TX_RECEIPT.contractAddress,
    abi=SMARTCONTRACT_INTERFACE['abi'],
)
```

[Back To Top](#table-of-contents)

## Using Flask to Build a dApp

[Back To Top](#table-of-contents)

### Setting up the Flask environment

In order to run the Flask application, some environment variables to run the Flask Webserver:

```
export FLASK_APP="dapp.py"
export FLASK_ENV=development
export FLASK_DEBUG=0
```
```dapp.py``` is going to be where the dApp is built.

### dapp.py

```
# Flask requirements
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired
```

```
# DAPP Requirements
from hexbytes import HexBytes
from web3.auto import w3
from deploycontract import ASSETREGISTER
```

The most important thing to notice from here is that ```deploycontract.py``` is imported as a python library.  More specifically this function is imported:

* ```ASSETREGISTER``` - 


[Back To Top](#table-of-contents)

#### Create Forms for Smart Contract Functions

##### Register Form
```
class RegisterForm(FlaskForm):
    ethaddress = SelectField('Ethereum Address', choices=[])
    serialnumber = StringField('Serial Number', [InputRequired()])
```

[Back To Top](#table-of-contents)

#### Application Routing - dapp.py

```dapp.py``` is the file that runs the Flask server for this demonstration. It provides the routing for our web application.  ```dapp.py``` also inherits the functions  of ```deploycontract.py```, which is the interface with the smart contract's functions. This is what provides the web browser interface between your dApp and the end user.


[Back To Top](#table-of-contents)

##### GET - / 

```
@app.route("/")
def home():
    return render_template('home.html', contractaddress=assetregister.address)
```

[Back To Top](#table-of-contents)

##### GET - /register


```
@app.route("/register", methods=['GET'])
def register():
    form = RegisterForm()
    form.ethaddress.choices = []
    n = -1
    for chooseaccount in w3.personal.listAccounts:
        n = n+1
        form.ethaddress.choices += [(n, chooseaccount)]
    return render_template('register.html', registerform=form, contractaddress=assetregister.address)
```

[Back To Top](#table-of-contents)

##### POST - /registered


```
def registered():
    registered = assetregister.functions.setRegistration(
        request.form['serialnumber'],
        w3.eth.accounts[int(request.form['ethaddress'])]).transact() # create the transaction
    tx =  w3.eth.getTransaction(registered)
    tx_hash = HexBytes.hex(tx['hash'])
    tx_data = HexBytes.hex(tx['input'])
    return render_template(
        'registered.html',
        reg_ethaddress=w3.eth.accounts[int(request.form['ethaddress'])],
        reg_serial=request.form['serialnumber'],
        reg_accountnumber=request.form['ethaddress'],
        reg_receipt=w3.eth.getTransactionReceipt(registered),
        reg_txhash= tx_hash,
        reg_txdata= tx_data,
        contractaddress=assetregister.address
    )
```

[Back To Top](#table-of-contents)

### Templates


#### index.html

This is the main template for the dApp when it is loaded in a browser.  Aside from some basic HTML and CSS, pay attention to the variable ```{{ contractaddress}}``` that is passed from dapp.py to the template.

```
<div class="w3-container w3-padding-small w3-theme-d3">
  <div class="w3-right">
      Contract Address: {{ contractaddress }}
  </div>
</div>
```

All of the other pages in this demo will inherit this template: home.html, register.html, registered.html.

It will display application information between these two tags in this file: 

```
{% block content %}{% endblock %}
```

[Back To Top](#table-of-contents)

#### home.html

This is nothing more than the landing page or "menu" for the other routes in the dApp.

```home.html```, like other templates are extensions of the ```index.html``` template:

```
{% extends 'index.html' %}
```
The template's content is then imported in between the block content tags:

```
{% block content %}
    <div class="w3-cell-row" align="center">
      <div class="w3-container w3-cell w3-mobile">
        <div class="w3-card">
          <p><a href="/register"><i class="fa fa-address-card fa-5x"></i>
          <br>REGISTER</a></p>
        </div>
      </div>
    </div>
{% endblock content %}
``` 
There is nothing interesting happening here. This is merely demonstrating how to insert some html content inbetween the ```{% block content %}``` and ```{% endblock content%}``` in ```index.html```.

[Back To Top](#table-of-contents)

#### register.html

This template provides the user input for the dApp. This is the template for our GET function.

Once the form is submitted, it will call the ```/registered``` route and pass that information to that function, and display the ```
``` template in the next section. This call to the template and route is represented by ```{{ url_for('registered') }}``` in the html form tags:

```
<form method="POST" action="{{ url_for('registered') }}" enctype="multipart/form-data">
```

Within the double-curly brackets in these templates, you can display vars, objects, and other information into the template from the python application.

What can be seen below is calling the ```RegisterForm``` class in ```dapp.py```.  Here is 'Ethereum Address' text label from that class, along with the drop-down field itself.

```
<td>{{ registerform.ethaddress.label }} :</td>
<td>{{ registerform.ethaddress }}</td>
```

The same thing happens for bringing up the serial number form field. This is a text string provided to the smart contract through this form. 

```
<td>{{ registerform.serialnumber.label }} :</td>
<td>{{ registerform.serialnumber }}</td>
```

These are the two values that will be passed to the smart contract. The Ethereum Address and the Serial Number (passed as a text string).

[Back To Top](#table-of-contents)

#### registered.html

This template is the one used for the ``POST`` request from ```register.html```.  Two variables are passed from ```dapp.py```
to this particular template. 

* ```reg_ethaddress``` displays the ethereum address used to make the transaction to the smart contract address. 

* ```reg_serial``` displays the serial number passed from the html form to the smart contract.

```
<br>REGISTERED</p>
Ethereum Address: {{ reg_ethaddress }} <br>
Serial Number: {{ reg_serial }} <br>
```

Within ```dapp.py```, not all variables are passed to this template. 

```
reg_receipt=w3.eth.getTransactionReceipt(registered),
reg_txhash= tx_hash,
reg_txdata= tx_data,
```

These can all be called in to the ```registered.html``` template with double curly brackets in the template. i.e.

```
Transaction Hash: {{ reg_txhash }} <br>
Transaction Data: {{ reg_txdata }} <br>
```

[Back To Top](#table-of-contents)

