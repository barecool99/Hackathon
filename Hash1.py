import hashlib
import os

salt = os.urandom(32)
password = 'password123'

key = hashlib.pbkdf2_hmac(
    'sha256',
    password.encode('utf-8'),
    salt,
    100000
)

storage = salt + key

salt_from_storage = storage[:32]
key_from_storage = storage[32:]

