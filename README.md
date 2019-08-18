<p align="center">
<img src="/media/bitcoinbay-logo-00.jpeg">
</p>
# Building dApps with Python, Flask, Solidity, & Web3.py

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
sudo pip3 install -r requirements.txt
```

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

### Get Familiar with Web3.py

Web3 is an API to the Ethereum Blockchain to build applications with.  There are many implementations. The most widely used implementation is Web3.js, which Web3.py is derrived from.  So let's get started with a python terminal: ```python3```

#### Import the Libraries

```
>>> from web3 import Web3, HTTPProvider
```

#### Set Ganache-CLI as the Ethereum Blockchain Provider

```
>>> web3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
```

#### Interacting with Ganache-GLI through Python with Web3.py

Get a list of current Ethereum Addresses:

```
>>> web3.personal.listAccounts
```

![Ganache-CLI Ethereum Addresses in Python3 Terminal](/media/ganache-cli-01.png)

Notice that this lists the ethereum addresses started by ganache-cli. The call from python to Web3.py can be observed from the ganache-cli terminal as well.

![Python Call can be seen in Ganache-cli](/media/ganache-cli-02.png)

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

#### Send ETH to New Account

Send some ETH to the new account:

```
>>> web3.eth.sendTransaction({'to': '0xE972Dc8a9a0701A98dB8466FC555Bc10150Cd977', 'from': web3.eth.coinbase, 'value': 1000000})
HexBytes('0xdd1ca7444da4498e168954669e3f1381f0a3843c40adaaa8e55d32e07c7c5985')
```
The response is the transaction hash registered on the blockchain.  Here is the output of the transaction in ganache-cli:

![Send ETH to new account](/media/ganache-cli-05.png)

#### More Web3.py Info

For more information and documentation on web3.py:
https://web3py.readthedocs.io/en/stable/index.html

## Explaining Solidity and Smart Contracts

Smart Contracts (simply put) are small computer programs.  These programs exist on a common blockchain. When triggered, they are self-executing. The terms of the contract between the contract owner and the recipient are expressed as code. Since Smart Contracts exist on a decentralized blockchain, they permit trusted transactions/agreements to be carried out without any need for a central authority, legal system, or enforcement mechanism.  However, due to the structure and security of this platform, there is little need for intermediaries.

This makes the transactions of a Smart Contract transparent, trustless, traceable, irreversable, and globally redundant.

### Solidity and Solc

#### Solidity

Solidity is statically typed, contract-oriented, and a high-level language for implementing smart contracts on the Ethereum platform.

Ethereum is by far the most popular platform for Solidity, but other platforms use Solidity, such as:  Hyperledger, Ethereum Classic, Monax, CounterParty (on Bitcoin), and even SWIFT has a proof-of-concept built using Solidity.

#### LLLC

LLLC, the Lovely Little Language Compiler. This binary will translate Solidity Contracts into a Ethereum-Blockchain executable format.  

#### Solc

Solc is a binary and commandline interface for the Solidity Compiler (LLLC). 

#### Py-Solc Library

Python wrapper around the solc Solidity compiler. Here is an integral part of building a python-based dApp. 

#### 

### Building A Contract

#### Sample Contract

```
pragma solidity ^0.4.24;
contract StorageContract {
    /* Define variable owner of the type address */
    string public serialnumber;
    address public assetowner;
    string public location;

    event Registration(
       string serialnumber,
       address assetowner
    );

    function setRegistration (string newSerialnumber, address newAssetowner) public {
        serialnumber = newSerialnumber;
        assetowner = newAssetowner;
        emit Registration(serialnumber, assetowner);

    }

    event Reporting(
       string serialnumber,
       string location,
       address assetowner
    );

    function setReporting (string newSerialnumber, string newLocation, address newAssetowner) public {
        serialnumber = newSerialnumber;
        location = newLocation;
        assetowner = newAssetowner;
        emit Reporting(serialnumber, location, assetowner);

    }
}

```

#### Learning More About Solidity

There are plenty of online resources for learning more about Solidity.  For exploring more, take a look at some of the provided documentation and sample contract-implementations:
* Solidity Documentation: https://solidity.readthedocs.io/en/v0.4.24/
* OpenZeppelin: https://github.com/OpenZeppelin/openzeppelin-contracts
* BlockGeeks: https://github.com/blockgeeks/workshop/tree/master/src/contracts

#### Inherting Other Contracts

### Deploying Contracts

There are two ways to deploy a contract with Python.  It can be done with the Solidity Contract code written directly inline in a Python application.  It can also be compiled from a ```.sol``` Solidity Contract file.

This section specifically breaks down deploycontract.py in this repository.

#### Deploying with Inline Solidity Code

Create a variable for the contract source code.  Create a set of triple quotes, and paste in the contract.

```
contract_source_code = '''
pragma solidity ^0.4.24;
contract StorageContract {
    /* Define variable owner of the type address */
    string public serialnumber;
    address public assetowner;
    string public location;

    event Registration(
       string serialnumber,
       address assetowner
    );

    function setRegistration (string newSerialnumber, address newAssetowner) public {
        serialnumber = newSerialnumber;
        assetowner = newAssetowner;
        emit Registration(serialnumber, assetowner);

    }

    event Reporting(
       string serialnumber,
       string location,
       address assetowner
    );

    function setReporting (string newSerialnumber, string newLocation, address newAssetowner) public {
        serialnumber = newSerialnumber;
        location = newLocation;
        assetowner = newAssetowner;
        emit Reporting(serialnumber, location, assetowner);

    }
}
'''
```

Compile the contract:

```
compiled_sol = compile_source(contract_source_code) # Compiled source code
```

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

#### Building the Contract Interface

```
smartcontract_interface = compiled_sol['<stdin>:StorageContract']
StorageContract = web3.eth.contract(abi=smartcontract_interface['abi'], bytecode=smartcontract_interface['bin'])
```

Setup the transaction to deploy the contract:

```
web3.eth.defaultAccount = web3.eth.accounts[0] # From which account?  The first one.
tx_hash = StorageContract.constructor().transact() # Transaction
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash) # Get the Transaction receipt
```

Create the Contract Instance:

```
assetregister = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=smartcontract_interface['abi'],
)
```


## Using Flask to Build a dApp


### Setting up the Flask environment

```
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
```

```
# DAPP Requirements
from hexbytes import HexBytes
from web3.auto import w3
from deploycontract import assetregister, StorageContract
```

### Flask Routing & Deployed Contracts

```
app = Flask(__name__)
bootstrap = Bootstrap(app)
dir_path = os.path.dirname(os.path.realpath(__file__))
app.config['SECRET_KEY'] ='TempSecretKey'
```

### Running the Flask Server

Before starting, Flask requires at least 3 environment variables provided:  Location of your app, type of environment, and debug level.

```
export FLASK_APP="dapp.py"
export FLASK_ENV=development
export FLASK_DEBUG=0
```

In order to run the webserver, type ```flask run --host=0.0.0.0```

![Starting Flask](/media/flask-00.png)

