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

