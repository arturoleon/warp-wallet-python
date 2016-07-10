from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import HMAC
from Crypto.Hash import SHA256
import binascii
import scrypt
import subprocess

def hmac_sha256(secret, salt):
	m = HMAC.new(secret, None, SHA256)
	m.update(salt)
	return m.digest()

def sxor(s1,s2):    
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def generate_address(passphrase, salt=""):
	data = scrypt.hash(passphrase + "\x01", salt + "\x01", 1 << 18, 8, 1, 32)

	out = PBKDF2(password=passphrase + "\x02",salt=salt + "\x02",
		dkLen=32, count=1 << 16, prf=hmac_sha256)

	merge = binascii.hexlify(sxor(data,out))

	p = subprocess.Popen(['bash', '-c', '. bitcoin.sh; newBitcoinKey 0x'+merge], stdout=subprocess.PIPE)
	result = p.communicate()[0].split("\n")

	return [result[10].split()[2], result[9].split()[1]]

output = generate_address("PuACRv0R")
print output
