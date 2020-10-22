import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

def Generate():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    message = b'{"name": "Satyam Anand", "email": "satymaanand@gmail.com", "Adhar"}'
    publickey = key.publickey() 
    print("Public Key : ", publickey)
    
    encryptor = PKCS1_OAEP.new(publickey)
    encrypted = encryptor.encrypt(message)
    print('encrypted :', encrypted)
    f = open ('encrypt.txt', 'w')
    f.write(str(encrypted)) 
    f.close()
    
    
    f = open('encrypt.txt', 'r')
    message = f.read()
    decryptor = PKCS1_OAEP.new(key)
    decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))
    print('Decrypted : ', decrypted)
    
    f = open ('encryption.txt', 'w')
    f.write(str(message))
    f.write(str(decrypted))
    f.close()

    hasher = SHA256.new(message)
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(hasher)
    print(signature)
Generate()    