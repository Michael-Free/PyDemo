# Building dApps with Python, Flask, and Solidity

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
from web3 import Web3, HTTPProvider
```

#### Set Ganache-CLI as the Ethereum Blockchain Provider

```
web3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
```
#### Interacting with Ganache-GLI through Python with Web3.py

Get a list of current Ethereum Addresses:
```
web3.personal.listAccounts
```
![Ganache-CLI Ethereum Addresses in Python3 Terminal](/media/ganache-cli-01.png)
Notice that this lists the ethereum addresses started by ganache-cli. The call from python to Web3.py can be observed from the ganache-cli terminal as well.
![Python Call can be seen in Ganache-cli](/media/ganache-cli-02.png)

#### Get Balances 

#### Create New Account

#### Send ETH to New Account

#### More Web3.py Info
For more information and documentation on web3.py:
https://web3py.readthedocs.io/en/stable/index.html

## Building Solidity Smart Contract(s)

Smart Contracts (simply put) are small computer programs.  These programs exist on a common blockchain. When triggered, they are self-executing. The terms of the contract between the contract owner and the recipient are expressed as code. Since Smart Contracts exist on a decentralized blockchain, they permit trusted transactions/agreements to be carried out without any need for a central authority, legal system, or enforcement mechanism.  This makes the transactions of a Smart Contract transparent, trustless, traceable and irreversible. 

### Solidity and Solc

Solidity is an language for writing smart contracts.  Ethereum is by far the most popular platform for Solidity, but other platforms use Solidity, such as:  Hyperledger, Ethereum Classic, Monax, CounterParty (on Bitcoin), and even SWIFT has a proof-of-concept built using it.

### Building Contracts

#### Learning More About Solidity

There are plenty of online resources for learning more about Solidity.  For exploring more, take a look at some of the provided documentation and sample contract-implementations:
* Solidity Documentation: https://solidity.readthedocs.io/en/v0.4.24/
* OpenZeppelin: https://github.com/OpenZeppelin/openzeppelin-contracts
* BlockGeeks: https://github.com/blockgeeks/workshop/tree/master/src/contracts

### Importing Contracts

### Deploying Contracts



## Using Flask to Build a dApp

### Setting up the Flask environment

Before starting, Flask requires at least 3 environment variables provided:  Location of your app, type of environment, and debug level.
```
export FLASK_APP="dapp.py"
export FLASK_ENV=development
export FLASK_DEBUG=0
```

In order to run the webserver, type ```flask run --host=0.0.0.0```

### Flask Routing & Deployed Contracts
