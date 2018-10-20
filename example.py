import warpwallet

private_key = warpwallet.generate_keypair("456789456", salt="123456")
wif = warpwallet.privkey_to_wif(private_key)
addr = warpwallet.key_to_addr(private_key)

print "WIF: {}, Private key: {}".format(wif, addr)
