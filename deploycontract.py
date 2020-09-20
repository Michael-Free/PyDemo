"""
Deploy Solidity Contract to Ganache-CLI
"""
# Import required libraries for compiling and deploying a smart contract
from solc import compile_source
from web3 import Web3, HTTPProvider

# set the provider (interface) to be used for web3 (ganache-cli)
WEB3 = Web3(HTTPProvider('http://127.0.0.1:8545'))

# provide the smart contract
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
# compile the solidity source code
COMPILED_SOL = compile_source(CONTRACT_SOURCE_CODE)
# create an interface for the compiled contracct
SMARTCONTRACT_INTERFACE = COMPILED_SOL['<stdin>:StorageContract']
#
StorageContract = WEB3.eth.contract(
    abi=SMARTCONTRACT_INTERFACE['abi'],
    bytecode=SMARTCONTRACT_INTERFACE['bin'])
# send eth from which account?
WEB3.eth.defaultAccount = WEB3.eth.accounts[0]
# get the transaction hash
TX_HASH = StorageContract.constructor().transact()
# get the transaction receipt and get information about the contract deployment
TX_RECEIPT = WEB3.eth.waitForTransactionReceipt(TX_HASH)
# create an object for the smart contract to be called and interacted with
ASSETREGISTER = WEB3.eth.contract(
    # get the contract address from the transaction address
    address=TX_RECEIPT.contractAddress,
    abi=SMARTCONTRACT_INTERFACE['abi'],
)
