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
