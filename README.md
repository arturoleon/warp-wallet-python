# WarpWallet in python
Implementation of WarpWallet in python. https://keybase.io/warp/

Install the required packages running `pip install -r requirements.txt`  

## Usage

**Generate PrivateKey**

`generate_keypair(passhprase [,salt])` 

example:
```
>>> from warpWallet import generate_keypair
>>> generate_keypair('YqIDBApDYME',salt='G34HqIgjrIc')
'da009602a5781a8795d55c6e68a4b4d52969a75955ea70255869dd17c3398592'
```

**Generate [WIF](https://en.bitcoin.it/wiki/Wallet_import_format) key and Address**
```
>>> from warpWallet import generate_keypair
>>> from keyUtils import keyToAddr,privateKeyToWif
>>> privateKey = generate_keypair("PuACRv0R")
>>> [privateKeyToWif(privateKey),
	keyToAddr(privateKey)]
['5K4z2kZZxxMZ4Tp6F8gqRTdcTezKdZSxVmRWtPthtDCtNbo4qnB', '1AdU3EcimMFN7JLJtceSyrmFYE3gF5ZnGj']
```