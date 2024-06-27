import base64
import os
from cryptography.fernet import Fernet

logo = f"""
 _______  __    _  _______  ______    ___   _______  _______                   
|       ||  |  | ||       ||    _ |  |   | |       ||       |                  
|    ___||   |_| ||       ||   | ||  |   | |    _  ||_     _|                  
|   |___ |       ||       ||   |_||_ |   | |   |_| |  |   |                    
|    ___||  _    ||      _||    __  ||   | |    ___|  |   |                    
|   |___ | | |   ||     |_ |   |  | ||   | |   |      |   |                    
|_______||_|  |__||_______||___|  |_||___| |___|      |___| 

                                 OR                   
 ______   _______  _______  _______  __    _  _______  ______    ___   _______  _______ 
|      | |       ||       ||       ||  |  | ||       ||    _ |  |   | |       ||       |
|  _    ||    ___||  _____||    ___||   |_| ||       ||   | ||  |   | |    _  ||_     _|
| | |   ||   |___ | |_____ |   |___ |       ||       ||   |_||_ |   | |   |_| |  |   |
| |_|   ||    ___||_____  ||    ___||  _    ||      _||    __  ||   | |    ___|  |   |
|       ||   |___  _____| ||   |___ | | |   ||     |_ |   |  | ||   | |   |      |   |
|______| |_______||_______||_______||_|  |__||_______||___|  |_||___| |___|      |___|   

 [i] Encript or Desencript | Autor : JohnnixGamer | Official Encripter v3.4
"""
os.system("cls")
print(logo)

key_file = 'datakey.key'
if not os.path.exists(key_file):
    key = Fernet.generate_key()
    with open(key_file, 'wb') as f:
        f.write(key)
else:
    with open(key_file, 'rb') as f:
        key = f.read()

def encrypt_text(text):
    f = Fernet(key)
    encrypted_text = f.encrypt(text.encode())
    return encrypted_text.decode()

def decrypt_text(encrypted_text):
    f = Fernet(key)
    decrypted_text = f.decrypt(encrypted_text.encode())
    return decrypted_text.decode()

while True:
    print("\n[-] Menú Interactivo")
    print("[1] $ Encriptar texto")
    print("[2] $ Desencriptar texto")
    print("[3] $ Salir")
    choice = input("[?] Selecciona una opcion: ")

    if choice == "1":
        text = input("[?] Ingrese el texto a encriptar: ")
        encrypted_text = encrypt_text(text)
        print("\n[i] Texto encriptado:", encrypted_text)
        os.system("pause > nul")
        os.system("cls")
        print(logo)
    elif choice == "2":
        encrypted_text = input("[?] Ingrese el texto encriptado: ")
        decrypted_text = decrypt_text(encrypted_text)
        print("\n[i] Texto desencriptado:", decrypted_text)
        os.system("pause > nul")
        os.system("cls")
        print(logo)
    elif choice == "3":
        break
    else:
        print("Opción inválida. Intente de nuevo.")
        os.system("pause > nul")
        os.system("cls")
        print(logo)