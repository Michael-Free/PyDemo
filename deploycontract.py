# Import required libraries for compiling and deploying a smart contract
from solc import compile_source
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract

# set the provider (interface) to be used for web3 (ganache-cli)
web3 = Web3(HTTPProvider('http://127.0.0.1:8545'))

# provide the smart contract
contract_source_code = '''
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
# compile the solidity source code
compiled_sol = compile_source(contract_source_code)
# create an interface for the compiled contracct
smartcontract_interface = compiled_sol['<stdin>:StorageContract']
#
StorageContract = web3.eth.contract(
    abi=smartcontract_interface['abi'],
    bytecode=smartcontract_interface['bin'])
# send eth from which account?
web3.eth.defaultAccount = web3.eth.accounts[0]
# get the transaction hash
tx_hash = StorageContract.constructor().transact()
# get the transaction receipt and get information about the contract deployment
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
# create an object for the smart contract to be called and interacted with
assetregister = web3.eth.contract(
    # get the contract address from the transaction address
    address=tx_receipt.contractAddress,
    abi=smartcontract_interface['abi'],
)
