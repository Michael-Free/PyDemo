registration: event({serialnumber: string[64],assetOwner: address})

serialnumber: public(string[64])
assetowner: public(address)

@public
def setRegistration(newSerialnumber: string[64], newAssetowner: address):
    self.serialnumber = newSerialnumber
    self.assetowner = newAssetowner
    log.registration(newSerialnumber,newAssetowner)
