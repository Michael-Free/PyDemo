# PyDemo

## Install Requirements
System requirements on Ubuntu Server 18.04 LTS

```
sudo apt install libz3-dev python3-dev python3-pip npm
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


### Start Ganache-CLI
Ganache is an ethereum blockchain emulator. it allows developers to make calls to an ethereum-like blockchain, without having to run a node.

```
ganache-cli
```

Ganache is an ethereum blockchain emulator. it allows developers to make calls to an ethereum-like blockchain, without having to run a node.

When it's started, it will generate 10 ETH Public Key addresses and their corresponding keys.  Each address will have 100 ETH by default.

Other information is displayed like HD Wallet, which can be used to import these accounts into a wallet or other applications (Metamask, Parity, etc).

For the purposes of this demonstration, we wont be going too deep into Gas Limits and Gas Prices.  If you would like to learn more about it, this is probably the most informative explanation: https://blockgeeks.com/guides/ethereum-gas/


###
In another terminal, navigate to the PyDemo repository

Now that Ganache is running, let's get familiar with Web3.py, which your application will use to interact with ethereum.









Startup a python3 prompt an

```


```

For more information and documentation on web3.py:
https://web3py.readthedocs.io/en/stable/index.html
