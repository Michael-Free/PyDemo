import json
from solc import compile_source
from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider
from web3.auto import w3
from web3.contract import ConciseContract

web3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
contract_source_code = '''
pragma solidity ^0.4.21;
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
compiled_sol = compile_source(contract_source_code) # Compiled source code
smartcontract_interface = compiled_sol['<stdin>:StorageContract']
StorageContract = web3.eth.contract(abi=smartcontract_interface['abi'], bytecode=smartcontract_interface['bin'])
web3.eth.defaultAccount = web3.eth.accounts[0]
tx_hash = StorageContract.constructor().transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
assetregister = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=smartcontract_interface['abi'],
)
