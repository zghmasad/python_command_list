import hashlib
import sys

secret = "This is the password or document text"
bsecret = secret.encode()
print(bsecret)
m = hashlib.md5()
print(m)
m.update(bsecret)

print(m.digest())
print(hashlib.md5(bsecret).digest())


from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(key)

f = Fernet(key)

message = b"Secrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go hereSecrets go here"


encrypted = f.encrypt(message)

print(encrypted)
print(f.decrypt(encrypted))
print(sys.getsizeof(message),sys.getsizeof(encrypted))

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding

private_key = rsa.generate_private_key(public_exponent=65537,
                                       key_size=4096,
                                       backend=default_backend())

public_key = private_key.public_key
print(public_key)

public_key = private_key.public_key()
print(public_key)

message = b"More secrets go here"

encrypted = public_key.encrypt(message,
                               padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA512()),
                                            algorithm=hashes.SHA512(),
                                            label=None))

print(encrypted)

decrypted = private_key.decrypt(encrypted,
                                padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA512()),
                                             algorithm=hashes.SHA512(),
                                             label=None))

print(decrypted)
