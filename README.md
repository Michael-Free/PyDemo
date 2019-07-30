# PyDemo

## Install Requirements
System requirements on Ubuntu Server 18.04 LTS

```
sudo apt install libz3-dev python3-dev python3-pip npm
```

This demo uses Solc 0.4.25.  You can install from below:

```
wget https://github.com/ethereum/solidity/releases/download/v0.4.25/solidity-ubuntu-trusty.zip
solc unzip solidity-ubuntu-trusty.zip -d /usr/bin/
```

Install Ganache - the test ethereum blockchain and pip3 requirements

```
sudo npm install -g ganache-cli
sudo pip3 install -r requirements.txt
```

## Getting Started

Start up Ganache, a test ethereum blockchain.
```
ganache-cli
```

Now that Ganache is running, let's get familiar with Web3.py, which your application will use to interact with ethereum.

Startup a python3 prompt: ```python3```

```

```

For more information and documentation on web3.py:
https://web3py.readthedocs.io/en/stable/index.html
