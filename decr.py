from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import os

#check de qual files tem na pasta

all_aim_files = []
path = ''

skip_files = ['decr.py', 'attack.py', 'private_key.pem', 'secret_key.key', 'setup.py', 
              'public_key.pem', 'private_key.pem', 'requirements.txt', 'genKeys.py',
              'attack', 'frozen_application_license.txt']

#check de qual files tem na pasta

for file in os.listdir():
    if os.path.isfile(file) and file not in skip_files:
        all_aim_files.append(file)

print(all_aim_files)

with open('private_key.pem', 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None
    )

def decrypt(file):
    return private_key.decrypt(
            file,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
        )
)

with open('secret_key.key', 'rb') as key:
    secret_key = key.read()
    
key_decr = decrypt(secret_key)

with open('secret_key.key', 'wb') as key:
    key.write(key_decr)


for file in all_aim_files:
    try:
        for file in all_aim_files:
            with open(file, 'rb') as file_x:
                content = file_x.read()
            
            content_dencr = Fernet(key_decr).decrypt(content)

            with open(file, 'wb') as file_x:
                file_x.write(content_dencr)
    except:
        continue

print('Recuperação realizado com sucesso')
