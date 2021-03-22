import hashlib

salt = b''
key = b''

password_to_check = 'password246'

new_key = hashlib.pbkdf2_hmac(
    'sha256',
    password_to_check.encode('utf-8'),
    salt,
    100000
)

if new_key == key:
    print('Password is correct')
else:
    print('Password is incorrect')

    