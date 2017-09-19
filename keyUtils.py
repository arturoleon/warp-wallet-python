import ecdsa, hashlib, utils

# Key Creatinon
def privateKeyToPubKey(s):
    sk = ecdsa.SigningKey.from_string(s.decode('hex'), curve=ecdsa.SECP256k1)
    return ('\04' + sk.verifying_key.to_string()).encode('hex')

def pubKeyToAddr(s,p):
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(s.decode('hex')).digest())
    return utils.base58CheckEncode(p, ripemd160.digest())

def keyToAddr(s,testnet=False):
	# see https://en.bitcoin.it/wiki/List_of_address_prefixes
	# ie: mainnet --> 0 and testnet --> 111
	prefix = 111 if testnet else 0 
	return pubKeyToAddr(privateKeyToPubKey(s),prefix)

def privateKeyToWif(key_hex):    
    return utils.base58CheckEncode(0x80, key_hex.decode('hex'))

def wifToPrivateKey(s):
    b = utils.base58CheckDecode(s)
    return b.encode('hex')