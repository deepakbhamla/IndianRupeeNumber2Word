import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from Crypto.Cipher import PKCS1_OAEP

def Generate():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    
    publickey = key.publickey() 
    print("Public Key : ", publickey)
    
    encryptor = PKCS1_OAEP.new(publickey)
    encrypted = encryptor.encrypt(f"b'input'")
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

Generate()    