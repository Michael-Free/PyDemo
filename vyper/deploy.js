const ethers = require('ethers')
let abi = [{"name": "registration", "inputs": [{"type": "string", "name": "serialnumber", "indexed": false}, {"type": "address", "name": "assetOwner", "indexed": false}], "anonymous": false, "type": "event"}, {"name": "setRegistration", "outputs": [], "inputs": [{"type": "string", "name": "newSerialnumber"}, {"type": "address", "name": "newAssetowner"}], "constant": false, "payable": false, "type": "function", "gas": 169829}, {"name": "serialnumber", "outputs": [{"type": "string", "name": "out"}], "inputs": [], "constant": true, "payable": false, "type": "function", "gas": 11449}, {"name": "assetowner", "outputs": [{"type": "address", "name": "out"}], "inputs": [], "constant": true, "payable": false, "type": "function", "gas": 573}]


let bytecode = "0x61031556600035601c52740100000000000000000000000000000000000000006020526f7fffffffffffffffffffffffffffffff6040527fffffffffffffffffffffffffffffffff8000000000000000000000000000000060605274012a05f1fffffffffffffffffffffffffdabf41c006080527ffffffffffffffffffffffffed5fa0e000000000000000000000000000000000060a052632e14fe5d60005114156102125734156100ac57600080fd5b60606004356004016101403760406004356004013511156100cc57600080fd5b60243560205181106100dd57600080fd5b5061014080600060c052602060c020602082510161012060006003818352015b8261012051602002111561011057610132565b61012051602002850151610120518501555b81516001018083528114156100fd575b5050505050506024356001556024356102405260406101e0526101e051610220526101408051602001806101e05161022001828460006004600a8704601201f161017b57600080fd5b50506101c06101e051610220015160a0818352015b60a06101c05111156101a1576101c2565b60006101c0516101e0516102400101535b8151600101808352811415610190575b505060206101e051610220015160206001820306601f82010390506101e05101016101e0527fbb39cc3c1316c48fbfc20d5f95e06a2ca321882b02e0643082fd32d2e402f95e6101e051610220a1005b63cead807560005114156102e457341561022b57600080fd5b60008060c052602060c020610180602082540161012060006003818352015b8261012051602002111561025d5761027f565b61012051850154610120516020028501525b815160010180835281141561024a575b505050505050610200610180516040818352015b60406102005111156102a4576102c0565b6000610200516101a001535b8151600101808352811415610293575b50506020610160526040610180510160206001820306601f8201039050610160f350005b63bcce1625600051141561030b5734156102fd57600080fd5b60015460005260206000f350005b60006000fd5b61000461031503610004600039610004610315036000f3"


let privateKey = ""
let provider = ethers.getDefaultProvider('rinkeby')
let wallet = new ethers.Wallet(privateKey, provider);

deploy()

async function deploy() {
  let factory = new ethers.ContractFactory(abi, bytecode, wallet);

    // Notice we pass in "Hello World" as the parameter to the constructor
    let contract = await factory.deploy();

    // The address the Contract WILL have once mined
    // See: https://ropsten.etherscan.io/address/0x2bd9aaa2953f988153c8629926d22a6a5f69b14e
    console.log(contract.address);
    // "0x2bD9aAa2953F988153c8629926D22A6a5F69b14E"

    // The transaction that was sent to the network to deploy the Contract
    // See: https://ropsten.etherscan.io/tx/0x159b76843662a15bd67e482dcfbee55e8e44efad26c5a614245e12a00d4b1a51
    console.log(contract.deployTransaction.hash);
    // "0x159b76843662a15bd67e482dcfbee55e8e44efad26c5a614245e12a00d4b1a51"

    // The contract is NOT deployed yet; we must wait until it is mined
    await contract.deployed()
}
