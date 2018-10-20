[![CircleCI](https://circleci.com/gh/arturoleon/warp-wallet-python.svg?style=svg)](https://circleci.com/gh/arturoleon/warp-wallet-python)

# WarpWallet in Python
Implementation of [WarpWallet](https://keybase.io/warp/) in Python. 

## Usage

Install the module by running `pip install warpwallet`

**Import module**
```
import warpwallet
```

**Generate PrivateKey**

```
warpwallet.generate_keypair(passhprase [,salt])
```

Example:
```
>>> import warpwallet
>>> warpwallet.generate_keypair('YqIDBApDYME', salt='G34HqIgjrIc')
'da009602a5781a8795d55c6e68a4b4d52969a75955ea70255869dd17c3398592'
```

**Generate [wallet import format (WIF)](https://en.bitcoin.it/wiki/Wallet_import_format) and address**
```
import warpwallet

private_key = warpwallet.generate_keypair("PuACRv0R")
wif = warpwallet.privkey_to_wif(private_key)
addr = warpwallet.key_to_addr(private_key)

print "WIF: {}, Address: {}".format(wif, addr)
```