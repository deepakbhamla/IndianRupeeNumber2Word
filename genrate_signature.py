import OpenSSL.crypto
import base64
from Crypto.PublicKey import RSA 
from Crypto.Signature import PKCS1_v1_5 
from Crypto.Hash import SHA256 
from base64 import b64decode 
import codecs

# Steps:: 
# 1. virtualenv venv
# 2. source venv/bin/activate

def load_public_key(pfx_path, pfx_password):
    ''' Read the keys and return as PEM encoded '''
    # print('Opening:', pfx_path)
    with open(pfx_path, 'rb') as f:     
            pfx_data = f.read()
            
    # print('Loading PFX contents:')
    p12 = OpenSSL.crypto.load_pkcs12(pfx_data, pfx_password)

    # ----------------------------------------------------------------------------------------
    # PEM - gives result in base 64 enoded ascii ????
    public_key = OpenSSL.crypto.dump_publickey(
            OpenSSL.crypto.FILETYPE_PEM,
            p12.get_certificate().get_pubkey())
    print("\nPUBLIC KEY EXTRACTED => ",public_key)
    # ----------------------------------------------------------------------------------------
    private_key = OpenSSL.crypto.dump_privatekey(
            OpenSSL.crypto.FILETYPE_PEM,
            p12.get_privatekey())
    print("\nPRIVATE KEY EXTRACTED => ",private_key)
    # ----------------------------------------------------------------------------------------
    certi = OpenSSL.crypto.dump_certificate(
            OpenSSL.crypto.FILETYPE_PEM,
            p12.get_certificate())
    print("\nCERTIFICATE EXTRACTED => ",certi)
    # ----------------------------------------------------------------------------------------
    URL = b"https://115.112.16.66/customer-service/v3/dan/checkDANStatus"
    # let this  is the url of line no 95 of .vb
   
    h = SHA256.new(URL)
    pvtkey = RSA.importKey(private_key)
    pubkey = RSA.importKey(public_key)
    
    signt = PKCS1_v1_5.new(pvtkey)
    signature = signt.sign(h)
    
    hexify = codecs.getencoder('hex')
    m = hexify(signature)[0]
    print(m)
    #it will generate a signature

load_public_key('./esign_Testing.pfx',"abhiraj")