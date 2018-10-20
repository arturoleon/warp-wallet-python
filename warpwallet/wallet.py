from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import HMAC, SHA256
import binascii
import scrypt


def hmac_sha256(secret, salt):
    m = HMAC.new(secret, None, SHA256)
    m.update(salt)
    return m.digest()


def sxor(s1,s2):    
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))


def generate_keypair(passphrase, salt=""):
    # s1 = scrypt(key=(passphrase||0x1), salt=(salt||0x1), N=2^18, r=8, p=1, dkLen=32)
    s1 = scrypt.hash(passphrase + "\x01", salt + "\x01", 1 << 18, 8, 1, 32)

    # s2 = pbkdf2(key=(passphrase||0x2), salt=(salt||0x2), c=2^16, dkLen=32, prf=HMAC_SHA256)
    s2 = PBKDF2(password=passphrase + "\x02",salt=salt + "\x02",
        dkLen=32, count=1 << 16, prf=hmac_sha256)
    return binascii.hexlify(sxor(s1,s2))