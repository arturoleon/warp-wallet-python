import ecdsa
import hashlib
import utils


# Key creation
def privkey_to_pubkey(s):
    sk = ecdsa.SigningKey.from_string(s.decode('hex'), curve=ecdsa.SECP256k1)
    return ('\04' + sk.verifying_key.to_string()).encode('hex')


def pubkey_to_addr(s, p):
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(s.decode('hex')).digest())
    return utils.base58CheckEncode(p, ripemd160.digest())


def key_to_addr(s, testnet=False):
    # see https://en.bitcoin.it/wiki/List_of_address_prefixes
    # ie: mainnet --> 0 and testnet --> 111
    prefix = 111 if testnet else 0
    return pubkey_to_addr(privkey_to_pubkey(s), prefix)


def privkey_to_wif(key_hex):
    return utils.base58CheckEncode(0x80, key_hex.decode('hex'))


def wif_to_privkey(s):
    b = utils.base58CheckDecode(s)
    return b.encode('hex')