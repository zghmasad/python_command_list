
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding

private_key = rsa.generate_private_key(public_exponent=65537,
                                       key_size=4096,
                                       backend=default_backend())

#public_key = private_key.public_key
#print(public_key)

public_key = private_key.public_key()
print(public_key)
pk=private_key.public_key
print(pk())
print(private_key.public_key)

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
