# WarpWallet in python
Implementation of WarpWallet in python. https://keybase.io/warp/

Install the required packages running `pip install -r requirements.txt`  
`generate_address(passhprase [,salt])` returns an array with the Bitcoin address and the private key in [WIF](https://en.bitcoin.it/wiki/Wallet_import_format).

## ToDo
* Remove the dependency of `bitcoin.sh`
* Add tests and create package